#VARIABLES
temperature =0.7 #float
max_tokens =1024  #int
is_streaming = False #bool
content_box = None #NoneType


#Type hints
model_name: str="gemini-2.0-flash" #str
tempearture: float = 0.7 #float
max_tokens:int=1024  #int
is_streaming:bool =False #bool
content_box: None =None  #NoneType

#strings:immutable|string formatting
#old version 
name ="LLM"
score=97.3
print("Hello %s" %name)
print("Score %.1f" %score)

#f-strings (Py 3.6+)
print(f"hello {name}")
print(f"score: {score:.1f}")

#expressions inside f-strings
world_limit =200
print(f"{'over' if world_limit>150 else 'under'}limit")
data={"topic":"Rag"}
print(f"Topic:{data['topic']}")

#type specifiers
pi=3.14159
print(f"pi:{pi:.2f}")

#debugging
temperature =0.7
print(f"temprature:{tempearture:.1f}")

# multiline f string formatting 
user_input ="what isn langchain?"
content_text="langchain is a framework"\
    "for building LLM apps"
System_prompt=f"""
you are a helpful AI tutor.
context provided:{content_text}
student question:{user_input}
instructions:
-answer based only on the context above
-if the answer is not in the context,say "i don't know"
-keep your answer under 3 sentences
""".strip()
print(System_prompt)


#lists:orderded,mutable,heterogenous sequences
#In Gen AI:Chat history,chunks of retreived documents
# Token sequences
chat_history:list[dict] =[
    {"rolr":"user","content":"what is an LLM"},
    {"role":"assistant","content":"a llm is a neural"
     "n/w trained on vast amount of text."},
]
#access
first_msg = chat_history[0]
print(first_msg)
print(chat_history[-1]["content"]) #last elements 

# modify
chat_history.append({"role":"user","content":"what is a rag"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#iterate 
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['conten']}")

# list of documents chunks
chunks:list[str]=[
    "rag stands for retrevial augmented generation",
    "it combine a retreiver with a generator",
]   

#filter chunks based on length 
valid_chunks =[c for c in chunks if len(c.split())>=6]
print(valid_chunks)