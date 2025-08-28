from flask import Flask, render_template, redirect, flash, request, session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

# configure apllication
app = Flask(__name__)
app.secret_key = "thesafestsecretkeyforyourrecipe"
# configure cs50 library to use sqlite database
db = SQL("sqlite:///recipes.db")

@app.route("/")
def index():
    if "user_id" not in session:
        return render_template("welcome.html")

    recipes = db.execute("SELECT * FROM recipes WHERE user_id = ?", session["user_id"])
    return render_template("index.html", recipes=recipes)


@app.route("/login", methods=["GET", "POST"])
def login():

    #forget any user_id
    session.clear()

    # user reached route via POST
    if request.method == "POST":
        if not request.form.get("username"):
            flash("Please provide username.")
            return redirect("/login")

        elif not request.form.get("password"):
            flash("Please provide password.")
            return redirect("/login")

        # query database for username
        rows = db.execute("SELECT * FROM users where username = ?", request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid username or password.")
            return redirect("/login")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]
        flash("Welcome back!")
        return redirect("/")

    # user reached route via GET
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()
    flash("You have been logged out.")
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            flash("Please fill all fields!")
            return redirect("/register")

        if password != confirmation:
            flash("Passwords don't match!")
            return redirect("/register")

        hash_password = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash_password)

            user = db.execute("SELECT id FROM users WHERE username = ?", username)
            session["user_id"] = user[0]["id"]
        except:
            flash("Username already exists.")
            return redirect("/register")

        flash("Registration successful!")
        return redirect("/")

    return render_template("register.html")



@app.route("/create", methods=["GET", "POST"])
def create():
    if "user_id" not in session:
        flash("You must be logged in to add a recipe.")
        return redirect("/login")

    if request.method == "POST":
        title = request.form.get("title")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        category = request.form.get("category")
        cooking_time = request.form.get("cooking_time")
        difficulty = request.form.get("difficulty")

        if not title or not ingredients or not instructions or not difficulty:
            flash("Please fill in all required fields.")
            return redirect("/create")

        user_id = session.get("user_id")


        db.execute("""
                   INSERT INTO recipes (user_id, title, ingredients, instructions, category, cooking_time, difficulty)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   """, user_id, title, ingredients, instructions, category, cooking_time, difficulty)

        flash("Recipe added successfully!")
        return redirect("/")

    return render_template("create.html")


@app.route("/delete/<int:recipe_id>")
def delete(recipe_id):
    if "user_id" not in session:
        flash("Please log in to delete recipes.")
        return redirect("/login")

    db.execute("DELETE FROM recipes WHERE id = ? AND user_id = ?", recipe_id, session["user_id"])
    flash("Recipe deleted successfully.")
    return redirect("/")


@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = db.execute("SELECT * FROM recipes WHERE id = ?", id)

    if not recipe:
        flash("Recipe not found")
        return redirect("/")

    return render_template("recipe.html", recipe=recipe[0])


if __name__ == "__main__":
    app.run(debug=True, port=5001)




