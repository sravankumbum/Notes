from collections import Counter
import re

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


RELATIONSHIPS = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings",
}

RELATIONSHIP_EMOJIS = {
    "Friends": "🤝",
    "Love": "❤️",
    "Affection": "😊",
    "Marriage": "💍",
    "Enemies": "⚡",
    "Siblings": "👫",
    "Please enter valid names (letters only).": "❓",
}


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z]", "", name.lower())


def unmatched_count(name_one: str, name_two: str) -> int:
    counter_one = Counter(name_one)
    counter_two = Counter(name_two)

    common = counter_one & counter_two
    common_count = sum(common.values())

    return (len(name_one) + len(name_two)) - (2 * common_count)


def flames_result(name_one: str, name_two: str) -> str:
    cleaned_one = normalize_name(name_one)
    cleaned_two = normalize_name(name_two)

    if not cleaned_one or not cleaned_two:
        return "Please enter valid names (letters only)."

    count = unmatched_count(cleaned_one, cleaned_two)
    if count == 0:
        return "Siblings"

    sequence = list("FLAMES")
    index = 0

    while len(sequence) > 1:
        index = (index + count - 1) % len(sequence)
        sequence.pop(index)

    return RELATIONSHIPS[sequence[0]]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        second_name = request.form.get("second_name", "").strip()
        return redirect(
            url_for(
                "result_page",
                first_name=first_name,
                second_name=second_name,
            )
        )

    return render_template("index.html")


@app.route("/result", methods=["GET"])
def result_page():
    first_name = request.args.get("first_name", "").strip()
    second_name = request.args.get("second_name", "").strip()

    if not first_name and not second_name:
        return redirect(url_for("index"))

    result = flames_result(first_name, second_name)
    emoji = RELATIONSHIP_EMOJIS.get(result, "✨")

    return render_template(
        "result.html",
        first_name=first_name,
        second_name=second_name,
        result=result,
        emoji=emoji,
    )


if __name__ == "__main__":
    app.run(debug=True)
