import streamlit as st
import pickle
from langchain.chains import RetrievalQAWithSourcesChain
import os
from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

st.title("Capillary Tech: User Documentation")
st.sidebar.title("Sub-sections")

subtopics = ["Introduction", "Loyalty+", "Engage+", "Insights+", "Capillary Data Platform", "Admin Controls",
             "Smart Store+"]

selected_subtopic = st.sidebar.radio("Select the domain you want to inquire about:", subtopics)
pickle_name = {"Introduction": "intro.pkl",
               "Loyalty+": "loyalty.pkl",
               "Engage+": "engage.pkl",
               "Insights+": "insights.pkl",
               "Capillary Data Platform": "cap_data.pkl",
               "Admin Controls": "admin.pkl",
               "Smart Store+": "smart.pkl"}

st.subheader(selected_subtopic)

main_placeholder = st.empty()
query = main_placeholder.text_input("Question: ")

llm = OpenAI(temperature=0.4, max_tokens=1500)

if query:
    pickle_path = pickle_name[selected_subtopic]
    # result = get_qa(query, pickle)

    if os.path.exists(pickle_path):
        with open(pickle_path, "rb") as f:
            vectorstore = pickle.load(f)
            # retriever = vectordb.as_retriever(score_threshold=0.7)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

            result = chain({"question": query}, return_only_outputs=True)

    # st.header("Answer")
    st.markdown("Answer")
    st.write(result["answer"])

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        st.subheader("For more details refer to the link given below: ")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.write(source)


