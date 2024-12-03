from flask import Flask, request,render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Feedback

app = Flask(__name__)
engine = create_engine('sqlite:///feedback.db')  
Session = sessionmaker(bind=engine)
@app.route('/')
def index():
    return render_template('page.html')

from sqlalchemy.exc import SQLAlchemyError

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    from sqlalchemy.exc import SQLAlchemyError

    try:
        name = request.form.get('name')
        email = request.form.get('email')
        date_of_stay = request.form.get('date')
        comment = request.form.get('commentaire')
        rating_proprete = request.form.get('noteProproté')
        rating_personnel = request.form.get('notePersonnel')

        
        app.logger.debug(f"Received form data: name={name}, email={email}, date={date_of_stay}, "
                         f"comment={comment}, rating_proprete={rating_proprete}, "
                         f"rating_personnel={rating_personnel}")

        if not all([name, email, date_of_stay, comment, rating_proprete, rating_personnel]):
            return "All fields are required", 400

        feedback = Feedback(
            name=name,
            email=email,
            date_of_stay=date_of_stay,
            comment=comment,
            rating_proprete=rating_proprete,
            rating_personnel=rating_personnel
        )

        session = Session()
        session.add(feedback)
        session.commit()
        return "Feedback submitted successfully!"
    except SQLAlchemyError as e:
        session.rollback()
        app.logger.error(f"Database error: {str(e)}")
        return f"An error occurred: {str(e)}", 500
    except Exception as e:
        app.logger.error(f"General error: {str(e)}")
        return f"An error occurred: {str(e)}", 500
    finally:
        session.close()


@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')
if __name__ == '__main__':
    
    app.run(debug=True)