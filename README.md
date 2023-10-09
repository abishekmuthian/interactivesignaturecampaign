# Interactive Signature Campaign

Interactive Signature Campaign is an low-code, easily deployable platform that engages signers directly with the cause, allowing them to provide their own authentic signatures with ease.

## Demo Video

![Interactive Signature Campaign powered by Dropbox Sign](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/thumbnail.png)

Clicking the above image will open the demo video in YouTube.

## Demo

[WWGM GNE Myopathy Campaign](https://interactivesignaturecampaign.streamlit.app/)

## Features

- Interactive Chat GPT + LlamaIndex powered chat bot to answer questions regarding your campaign.
- Get signatures from your signers interactively.
- Signed petitions delivered to your email.
- Easy one click deployment.
- Low code, publish your interactive signature campaign with just markdown and toml files.

## Screenshots

Signature campaign page
![World Without Myopathy GNE Myopathy campaign](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/1.gif)

Interactive Chat Bot to answer questions on your signature campaign
![Interactive chat bot](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/2.png)

![Interactive chat bot](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/3.png)

![Interactive chat bot](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/4.png)

Petition letter sent to the signee
![Petition letter sent to the signee](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/5.png)

### Powered by Dropbox Sign

Signee can sign in real-time
![Signee can sign in real-time](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/6.png)

Signed petition letter received by the campaign organizer
![Signed petition letter received by the campaign organizer](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/7.png)

Create a template on Dropbox Sign for the petition letter
![Create template on Dropbox Sign](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/8.png)

Copy the template ID
![Create template on Dropbox Sign](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/9.png)

### Requirements

1.Python.

2.[Dropbox Sign](https://app.hellosign.com/account/signUp) API Key.

3.[Open AI Chat GPT](https://platform.openai.com/) API Key.

4.[Streamlit](https://streamlit.io) account.

## Setup

1.Clone the project.

```
$ git clone https://github.com/abishekmuthian/interactivesignaturecampaign.git
```

2.Navigate to the project and setup venv.

```
$ cd interactivesignaturecampaign
$ python -m venv .venv
$ pip install -r requirements.txt
```

3.Run the app using streamlit.

```
$ streamlit run streamlit_app.py
```

4.Add `.streamlit/secrets.toml`

5.Configuration
| Key | Value |Example|
|---|---|---|
|openai_key|Open AI Chat GPT Key|sk-xxxxxx|
|dropbox_sign_key|Dropbox Sign API Key |xxxxxx|
|template_id|Template ID from Dropbox Sign|xxxxxx|
|title|Title for the campaign|World Without GNE Myopathy|
|email_subject|Subject for the email through which the petition would be sent to the signee|WWGM sign the petition!|
|email_message|Message to be sent with the petition email|By signing this petition, you not only lend your voice to the countless individuals affected by GNE Myopathy but also champion the cause for an inclusive healthcare system in India. Together, we can pave the way for better diagnosis, treatment, and support. Stand with us in urging the Indian Government to recognize and include GNE Myopathy in its Rare Diseases Policy.|
|signer_role|Role declared for signee in the the Dropbox Sign, Must be 'Signee'|Signee|
|bot_spinner|Text to display when the bot is indexing data|Loading and indexing the GNE Myopathy faqs from WWGM – hang tight! This should take 1-2 minutes.|
|bot_intro|Intro message displayed by the bot|Ask me a question about this campaign and GNE Myopathy!|
|bot_context|System context for the bot for better accuracy of the answers|You are an expert on the GNE Myopathy and your job is to answer health questions. Assume that all questions are related to the GNE Myopathy. Keep your answers medical and based on facts – do not hallucinate diseases.|

## Deployment

1. Click deploy on the top right and follow the on screen instructions to deploy the app on streamlit community cloud.

![Click on the deploy button to deploy](https://interactivesignaturecampaign.s3.us-east-2.amazonaws.com/10.png)

2. Copy your secrets `./streamlit/secrets.toml` from to streamlit's secrets section.

## LICENSE

The MIT License (MIT)

Copyright (c) 2023 ABISHEK MUTHIAN(Interactive Signature Campaign)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
