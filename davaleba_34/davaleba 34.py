@app.route('/')
def main_page():
    users = User.query.with_entities(User.full_name, User.email).all()
    return render_template('main_page.html', users=users)