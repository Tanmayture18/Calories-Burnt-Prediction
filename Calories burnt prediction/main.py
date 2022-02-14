from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
file=open('model.pk1','rb')
rr=pickle.load(file)
file.close()

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        mydict=request.form
        Gender=(mydict['Gender'])
        Age=int(mydict['Age'])
        Height=int(mydict['Height'])
        Weight=int(mydict['Weight'])
        Duration=int(mydict['Duration'])
        Heart_Rate=int(mydict['Heart_Rate'])
        Body_Temp=int(mydict['Body_Temp'])
        
        
        inputfeatures=[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]
        CPred=rr.predict([inputfeatures]) 
        for i in CPred:
            cp=i #
        print(cp)
        #Gender	Age	Height	Weight	Duration	Heart_Rate	Body_Temp	Calories
   
        return render_template('show.html',inf=cp)#
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)   