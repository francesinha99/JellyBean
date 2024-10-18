from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for jelly bean flavors
jelly_beans = []

@app.route('/')
def index():
    return render_template('index.html', jelly_beans=jelly_beans)

@app.route('/add', methods=['POST'])
def add():
    flavor = request.form.get('flavor')
    if flavor:
        jelly_beans.append(flavor)  # Add new flavor to the list
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        flavor = request.form.get('flavor')
        if flavor:
            jelly_beans[index] = flavor  # Update the flavor at the given index
        return redirect(url_for('index'))
    return render_template('edit.html', flavor=jelly_beans[index], index=index)

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(jelly_beans):
        jelly_beans.pop(index)  # Remove the flavor from the list
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
