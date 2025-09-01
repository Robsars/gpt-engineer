from flask import Flask, render_template, redirect, url_for, request
from models import Todo
from forms import TodoForm, DeleteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory storage for todo items
todos = []

def create_app():
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = TodoForm()
        delete_form = DeleteForm()
        if form.validate_on_submit():
            new_todo = Todo(title=form.title.data)
            todos.append(new_todo)
            return redirect(url_for('index'))
        return render_template('index.html', todos=todos, form=form, delete_form=delete_form)

    @app.route('/delete/<int:todo_id>', methods=['POST'])
    def delete_todo(todo_id):
        if 0 <= todo_id < len(todos):
            del todos[todo_id]
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    create_app().run(debug=True)