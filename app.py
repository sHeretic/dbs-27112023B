#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[ ]:


from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"]) # decorator
def index():
    if request.method == "POST":
            rate = float(request.form.get("rate")) # this word "rate" at the backend must be the same as the frontend
            print(rate) # to confirm on the result; required due to the "waskey" as it travels through ICP
            return(render_template("index.html",result=-50.6*rate + 90.2))
    else:
        return(render_template("index.html",result="waiting for exchange rate..."))

if __name__ == "__main__":
    app.run()


# In[ ]:




