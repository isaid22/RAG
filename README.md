# RAG 

## Requirements
in this directory, you need to create a `.env` file that contains OpenAI API Key. The file should have the following content:

```
OPENAI_API_KEY="<your OpenAI API Key>"
```

Also, you might see the following error:

```
  File "/home/xps15/ai_venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 715, in urlopen
    httplib_response = self._make_request(
  File "/home/xps15/ai_venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 404, in _make_request
    self._validate_conn(conn)
  File "/home/xps15/ai_venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 1058, in _validate_conn
    conn.connect()
  File "/home/xps15/ai_venv/lib/python3.10/site-packages/urllib3/connection.py", line 363, in connect
    self.sock = conn = self._new_conn()
  File "/home/xps15/ai_venv/lib/python3.10/site-packages/urllib3/connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x7c9f6ef9dd50>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution
```

in which case, you might try turn off your VPN.

## Instruction

Run the following commend to build a `chroma` directory:

```
python create_db.py
```
After the completion, you will find a `chorma` directory. This is the vector database built with the documents you provided.

Now you may run a query:

```
python query_data.py "does Snap compete with TikTok?"
```

and the following is an example result:

```
Human: 
Answer the question based only on the following context:

competitors also include platforms that offer, or will offer, a variety of products, services, content, and online advertising 
offerings that compete or may compete with Snapchat features or offerings. For example, Instagram, a competing

---

share through Snapchat to develop or work with competitors to develop products or features that compete with us. Certain 
competitors, including Alphabet, Apple, and Meta, could use strong or dominant positions in one or more market segments

---

ephemeral products into its various platforms which mimic other aspects of Snapchat’s core use case. We also compete for 
users and their time, so we may lose users or their attention not only to companies that offer products and services that

---

Answer the question based on the above context: Does Snap compete with Tiktok

/home/xps15/ai_venv/lib/python3.10/site-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.chat_models.openai.ChatOpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import ChatOpenAI`.
  warn_deprecated(
/home/xps15/ai_venv/lib/python3.10/site-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The function `predict` was deprecated in LangChain 0.1.7 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
Response: Based on the context provided, it does not mention Tiktok as a competitor of Snapchat. The competitors mentioned include Instagram, Alphabet, Apple, and Meta.
Sources: ['pdf/NYSE_SNAP_2022.pdf', 'pdf/NYSE_SNAP_2022.pdf', 'pdf/NYSE_SNAP_2022.pdf']
```