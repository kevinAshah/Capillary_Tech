# Capillary Tech User Documentaion

This is an interactive platform where you can ask any question about the user documentation of the company Capillary Technologies and get and apt answer. Users can choose the subtopic and ask relevant question about the selected subtopic in the space given. The chatbot will present to you the answer for the question and the sources refered.

## Working of the Streamlit App
* Select a subtopic from the left pane. These is the list of main service soffered by Capillary Technologies (link to the main documentation page of Capillary Technologies is mentioned here : https://docs.capillarytech.com/docs/introduction). User can choose the subtopic they want to inquire about.  
* Enter the question in the space given and press enter.
* The answer to the question and the link to the sources which were refered to get the answer will be diplayed below the question.

## Features
* Load URLs of each service documentation in separate lists to fetch article content.
* Process article content through LangChain's UnstructuredURL Loader.
* Text splitting using RecursiveCharacterTextSplitter of Langchain
* Construct an embedding vector using OpenAI's embeddings and leverage FAISS (Facebook AI Similarity Search), a powerful similarity search library, to enable swift and effective retrieval of relevant information.
* Used RetrievalQA for retrieving the answers from the respective vector stores
* Interact with the LLM by inputting queries and receiving answers for the respective subtpic.

## Project Structure
* main.py - This is the main file and contains the code for streamlit app. It also contains the driver code for intializing the LLM model, reading the question, loading the pickle files and retrieving the answer and source URLs using the RetrievalQAWithSourcesChain library.
* helper.py - All the URLs for all the subtopics are mentioned here. These URLs are loaded and the content inside them is splitted and embedded. These embeddings are stored in the respective pickle files which are then loaded in the main.py file mentioned above to retrieve the answers.
* admin.pkl, cap_data.pkl, engage.pkl, insights.pkl, intro.pkl, loyalty.pkl, smart.pkl - These are the pickle files containing the embeddings made in the helper.py file.
* requirements.txt - This file contains all the libraries required to run the code and the streamlit app. You can install these libraries by running the ```pip install -r requirements.txt```.
* .env -  Configuration file to store the OPENAI_API_KEY.

## Installation
1. Clone the repository on your local machine
   
   ```bash
   git clone https://github.com/kevinAshah/Capillary_Tech.git
   ```
2. Navigate to the project directory

   ```bash
   cd Capillary_Tech
   ```
3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key by creating a .env file in the project root and adding your API

   ```bash
     OPENAI_API_KEY=your_api_key_here
   ```
5. Run the streamlit app on your local system

   ```bash
   streamlit run main.py
   ```

## Example Questions
You can ask the following questions to the LLM:
1. Introduction - What is Capillary Tech?
2. Loyalty+ - Types of Loyalty Programs supported by Capillary Tech
3. Engage+ - You can use creative management for multiple usages of templates like?
4. Insights+ - What is Databricks?
5. Capillary Data Platform - What is Connect+?
6. Admin Controls - What is Single Sign-On(SSO)?
7. Smart Store+ - Tell me something about visitorsense
