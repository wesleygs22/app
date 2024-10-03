from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def aluno_form(): 
    return render_template('aluno.html') 
if __name__ == '__main__': 
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def aluno_form():
    return render_template('aluno.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
   
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    email = request.form.get('email')
    curso = request.form.get('curso')
    
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)





