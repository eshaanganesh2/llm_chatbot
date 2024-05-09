import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# Replicate Credentials
with st.sidebar:
    st.title('🦙💬 Llama 2 Chatbot')
    # if 'REPLICATE_API_TOKEN' in st.secrets:
    if os.environ.get('REPLICATE_API_TOKEN'):
        st.success('API key already provided!', icon='✅')
        # replicate_api = st.secrets['REPLICATE_API_TOKEN']
        replicate_api= os.environ.get('REPLICATE_API_TOKEN')
        user_id = st.text_input('Enter your username', type='default')
        os.environ['USER_ID'] = user_id
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        user_id = st.text_input('Enter your username', type='default')
        if not (replicate_api.startswith('r8_') or len(replicate_api)==40 or len(user_id)>0):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
            os.environ['REPLICATE_API_TOKEN'] = replicate_api
            os.environ['USER_ID'] = user_id

    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=32, max_value=128, value=120, step=8)
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Please input report name, amount, date, XTHHSA and account numbers", "userId":user_id}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?", "userId":user_id}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

def verify_reportName():
    string_dialogue="As an obedient assistant, your task is strictly to return the report name if a value for Report name is provided in the prompt. Return NO if there is no value for report name in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    full_response = ''
    for item in output:
        full_response += item
    print("verify_reportName")
    print(full_response)
    if 'the report name is' in full_response:
        parts=full_response.split('the report name is',1)
        if len(parts)>1:
            print(parts[1].split()[0])
    else:
        print("NO")
        print(full_response)

    
def verify_amount():
    string_dialogue="As an obedient assistant, your task is strictly to return the amount if a value for amount is provided in the prompt. Return NO if there is no value for amount in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    
    full_response = ''
    for item in output:
        full_response += item
    print("verify_amount")
    print(full_response)
    if 'the amount is' in full_response:
        parts=full_response.split('the amount is',1)
        if len(parts)>1:
            print(parts[1].split()[0])
    else:
        print("NO")
        print(full_response)

def verify_fromDate():
    string_dialogue="As an obedient assistant, your task is strictly to return the from date if a value for from date is provided in the prompt. Return NO if there is no value for from date in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    
    full_response = ''
    for item in output:
        full_response += item
    print("verify_fromDate")
    print(full_response)
    if 'the from date is' in full_response:
        parts=full_response.split('the from date is',1)
        if len(parts)>1:
            print(parts[1].split()[0])
    else:
        print("NO")
        print(full_response)

def verify_toDate():
    string_dialogue="As an obedient assistant, your task is strictly to return the to date if a value for to date is provided in the prompt. Return NO if there is no value for to date in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    
    full_response = ''
    for item in output:
        full_response += item
    print("verify_toDate")
    print(full_response)
    if 'the to date date is' in full_response:
        parts=full_response.split('the to date date is',1)
        if len(parts)>1:
            print(parts[1].split()[0])
    else:
        print("NO")
        print(full_response)

def verify_xthhsa():
    string_dialogue="As an obedient assistant, your task is strictly to return the XTHHSA if a value for XTHHSA is provided in the prompt. Return NO if there is no value for XTHHSA in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    
    full_response = ''
    for item in output:
        full_response += item
    print("verify_xthhsa")
    print(full_response)
    if 'the xthhsa is' in full_response:
        parts=full_response.split('the xthhsa is',1)
        if len(parts)>1:
            print(parts[1].split()[0])
    else:
        print("NO")
        print(full_response)
    
def verify_account_numbers():
    string_dialogue="As an obedient assistant, your task is strictly to return the account number(s) if a value for account number(s) is provided in the prompt. Return NO if there is no value for account number(s) in the prompt. Your response must solely be dependent upon the text provided in the prompt and not be affected by any other factor. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    
    full_response = ''
    for item in output:
        full_response += item
    print("verify_account_numbers")
    print(full_response)
    if 'the account numbers are' in full_response or 'the account number is':
        parts1=full_response.split('the account number is',1)
        parts2=full_response.split('the account numbers are',1)
        if len(parts1)>1:
            print(parts1[1].split()[0])
        if len(parts2)>1:
            print(parts2[1].split()[0])
    else:
        print("NO")
        print(full_response)

# Function for generating LLaMA2 response. Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama2_response(prompt_input):
    #string_dialogue = "You are a helpful assistant. Your sole purpose is to receive Report name, amount, from date, to date and account number(s) from the user. The description of each of these fields is as follows: 1) Report name can be either ABC, DEF or GHI. 2) Amount is any numeric value 3) From date and to date is of the format dd/mm/yyyy 4) Account number is 12 digits long number. You must also make sure that the value for all the fields is obtained in the right format. You are only permitted to ask the user for each of the required fields until they are successfully retrieved in the required format. Do not interact with the user for any other reason whatsover."
    #string_dialogue="You are an obedient assistant. Your sole purpose is to receive Report name, amount, from date, to date, XTHHSA and account number(s) from the user in the required format. The required format for each of these fields is as follows: 1) Report name must be either ABC, DEF or GHI. 2) Amount must be numeric 3) From date and to date must be of the format dd/mm/yyyy 4) XTHHSA is of the form XXXX-XXXX-XXXX-XXXX where X is either an uppercase letter or a digit 5) Account number must be 12 digits long number. Do not interact with the user for any other reason whatsover and do not seek confirmation or suggest any changes on the requirements or the specified format. Ask the user for value of a field if not provided already. Return the value of the fields received so far in JSON format."
    #string_dialogue="As an obedient assistant, your task is strictly to gather Report name, amount, from date, to date, XTHHSA, and account number(s) from the user. Do not seek confirmation of values provided by the user. Do not suggest or raise any issues regarding the values provided by the user. Do not engage with the user for any other purpose. You may keep asking the user to provide values of fields that have not been received yet. List out the values for the following fields: Report name, amount, from date, to date, XTHHSA, and account number(s)."
    string_dialogue="As an obedient assistant, your task is strictly to gather Report name, amount, from date, to date, XTHHSA, and account number(s) from the user. Do not seek confirmation of values provided by the user. You may keep asking the user to provide values of fields that have not been received yet. Do not engage or interact with the user at all for any other purpose. You may safely assume that all values provided are correct and in the right format."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            if dict_message["userId"]==user_id:
                #string_dialogue += "User: " + dict_message["content"] + "\n\n"
                # string_dialogue += dict_message["content"] + "\n\n"
                string_dialogue += dict_message["content"]+". "
    #     else:
    #         if dict_message["userId"]==user_id:
    #             string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    verify_reportName()
    verify_amount()
    verify_fromDate()
    verify_toDate()
    verify_xthhsa()
    verify_account_numbers()

    print(string_dialogue)
    print("========================")
    print("End of history")
    print("========================")
    
    # verify_amount()
    # verify_fromDate()
    # verify_toDate()
    # verify_xthhsa()
    # verify_account_numbers()
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt, "userId":user_id})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response, "userId":user_id}
    st.session_state.messages.append(message)