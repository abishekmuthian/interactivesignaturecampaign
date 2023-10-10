from pathlib import Path
import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
import re
from pprint import pprint
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

# Set page layout to wide mode
st.set_page_config(layout="wide", page_icon = './images/logo.png', initial_sidebar_state="collapsed")

# Three columns with different widths for logo and title
col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.image('./images/logo.png')

col1, col2, col3 = st.columns([3,1,1])

with col1:    
    st.title(st.secrets["title"])


# Access the markdown files and display them
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("./data/index.md")
st.markdown(intro_markdown, unsafe_allow_html=True)


# Three columns with same widths for centering
col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.header('Your Signature Matters!')

    # Full Name Input
    full_name = st.text_input("Full Name:")

    # Basic validation for full name (checks if it's not empty and has at least two words)
    if full_name:
        names = full_name.split()
        if len(names) < 2:
            st.warning("Please enter your full name (at least first and last name).")

    # Email Input
    email = st.text_input("Email:")

    # Basic validation for email using a regex pattern
    EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if email and not re.match(EMAIL_REGEX, email):
        st.warning("Please enter a valid email address.")

    # If the validation is successful
    if full_name and email and len(full_name.split()) >= 2 and re.match(EMAIL_REGEX, email):
        # Do something, e.g., save the data, send an email, etc.
        if st.button("Sign campaign"):
            # Dropbox Sign, Send signature request
            configuration = Configuration(
            # Configure HTTP basic authorization: api_key
            username=st.secrets["dropbox_sign_key"],
            )

            with ApiClient(configuration) as api_client:
                signature_request_api = apis.SignatureRequestApi(api_client)

                signer_1 = models.SubSignatureRequestTemplateSigner(
                    role=st.secrets["signer_role"],
                    email_address=email,
                    name=full_name,
                )

                signing_options = models.SubSigningOptions(
                    draw=True,
                    type=True,
                    upload=True,
                    phone=False,
                    default_type="draw",
                )

                if st.secrets["template_id"]:
                    template_id = st.secrets["template_id"]

                    data = models.SignatureRequestSendWithTemplateRequest(
                    template_ids = [template_id],
                    subject=st.secrets["email_subject"],
                    message=st.secrets["email_message"],
                    signers=[signer_1],
                    signing_options=signing_options,
                    test_mode=True,
                )

                    try:
                        response = signature_request_api.signature_request_send_with_template(data)
                        pprint(response)
                        st.success("Petition letter was sent to your email for signature!")
                    except ApiException as e:
                        print("Exception when calling Dropbox Sign API: %s\n" % e)
                else:
                    st.error("Template id missing, Please set it in the environment")

    

st.markdown("---") 

#Access the OpenAI key from secrets
openai.api_key = st.secrets["openai_key"]

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": st.secrets["bot_intro"], "avatar":"./images/logo.png"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text=st.secrets["bot_spinner"]):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=st.secrets["bot_context"]))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()
# chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True, system_prompt= st.secrets["bot_context"]")

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    if message["role"] == "assistant": #Setting logo for the chat for role assistant
        with st.chat_message(message["role"],avatar="./images/logo.png"):
            st.write(message["content"])
    elif message["role"] == "user":
        with st.chat_message(message["role"], avatar="🧑‍💻"):        
            st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant",avatar="./images/logo.png"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history

# Set the sidebar for navigation
st.sidebar.title("Interactive Signature Campaign")
st.sidebar.markdown("Get your own low code Interactive Signature Campaign from [GitHub](https://github.com/abishekmuthian/interactivesignaturecampaign).")
st.sidebar.write("Built by Abishek Muthian.")
st.sidebar.markdown("---") 
st.sidebar.markdown("Powered by [Dropbox Sign](https://www.hellosign.com/features).")


