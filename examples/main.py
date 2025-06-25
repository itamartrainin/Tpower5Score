import tpower5score

if __name__ == '__main__':
    topics_set = [
        "Youth Activism",
        "Climate Change"
    ]

    docs = [
        "Dozens of high school students gathered along the coast of California this weekend to remove over 500 pounds "
        "of plastic waste. Organized by a local youth environmental group, the initiative aims to reduce ocean "
        "pollution and raise awareness about climate change. 'We're the generation that will live with the "
        "consequences,' said Maya Chen, 17, one of the event's organizers.",
        "More than 20,000 young protesters flooded the streets of Berlin in a climate march demanding stronger "
        "environmental legislation. The demonstration, part of the global Fridays for Future movement, called on "
        "lawmakers to phase out coal by 2030 and expand green energy initiatives. Activist Elias Bauer, 16, stated, "
        "'We want a future that is not on fire.'",
        "A coalition of student organizations from five continents submitted a petition to the United Nations this "
        "week, urging immediate and binding commitments to reduce global carbon emissions. The petition has already "
        "garnered over 1 million signatures. The youth leaders behind the movement say they are tired of waiting for "
        "older generations to act."
    ]

    agg_weights = {
        'Interpretability': 0.2,
        'Topic Coverage': 0.2,
        'Document Coverage': 0.2,
        'Overlap': 0.2,
        'Rank': 0.2
    }

    aspects, agg_score = tpower5score.evaluate(topics_set, docs)

    print(f'Aspects Scores: {aspects}')
    print(f'Aggregate Score: {agg_score}')
