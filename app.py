from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def hello():
    message = "Текст до получения результатов с формы"
    if request.method == "POST":
        age = request.form.get("age")
        message = f"Вы ввели возраст: {age}"
        # message = "Вы ввели возраст " + str(age)
        # message = "Вы ввели возраст {}".format(str(age))

    return render_template("index.html", message=message)
