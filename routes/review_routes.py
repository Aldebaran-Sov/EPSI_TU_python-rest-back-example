from flask import Blueprint, request, jsonify
from models.database import db
from models.review import Review

review_routes = Blueprint("review_routes", __name__)

@review_routes.route("/reviews", methods=["GET"])
def get_reviews():
    rating_filter = request.args.get("rating")
    if rating_filter:
        min_rating, max_rating = map(int, rating_filter.split('-'))
        reviews = Review.query.filter(Review.rating.between(min_rating, max_rating)).all()
    else:
        reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

@review_routes.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = Review.query.get(review_id)
    if review:
        return jsonify(review.to_dict()), 200
    return jsonify({"error": "Review not found"}), 404

@review_routes.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    if not data.get("title") or not data.get("rating"):
        return jsonify({"error": "Title and rating are required"}), 400

    new_review = Review(title=data["title"], rating=data["rating"], comment=data.get("comment"))
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@review_routes.route("/reviews/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()
    review.title = data.get("title", review.title)
    review.rating = data.get("rating", review.rating)
    review.comment = data.get("comment", review.comment)
    db.session.commit()
    return jsonify(review.to_dict()), 200

@review_routes.route("/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully"}), 200

@review_routes.route("/reviews/<int:review_id>/helpful", methods=["POST"])
def mark_review_as_helpful(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    review.helpful_count += 1
    db.session.commit()
    return jsonify({"message": "Marked as helpful"}), 200

@review_routes.route("/reviews/average", methods=["GET"])
def get_average_rating():
    average_rating = db.session.query(db.func.avg(Review.rating)).scalar()
    return jsonify({"average_rating": round(average_rating, 1)}), 200

@review_routes.route("/reviews/<int:review_id>/comments", methods=["POST"])
def add_comment_to_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()
    comment = data.get("comment")
    if not comment:
        return jsonify({"error": "Comment is required"}), 400

    review.comment = comment
    db.session.commit()
    return jsonify({"message": "Comment added", "comment": comment}), 201
