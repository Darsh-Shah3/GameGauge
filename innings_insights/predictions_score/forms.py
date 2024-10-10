from django import forms

# Lists of teams and cities
TEAM_CHOICES = [
    ('Royal Challengers Bengaluru', 'Royal Challengers Bengaluru'),
    ('Gujarat Titans', 'Gujarat Titans'),
    ('Lucknow Super Giants', 'Lucknow Super Giants'),
    ('Punjab Kings', 'Punjab Kings'),
    ('Delhi Capitals', 'Delhi Capitals'),
    ('Sunrisers Hyderabad', 'Sunrisers Hyderabad'),
    ('Chennai Super Kings', 'Chennai Super Kings'),
    ('Rajasthan Royals', 'Rajasthan Royals'),
    ('Kolkata Knight Riders', 'Kolkata Knight Riders'),
    ('Mumbai Indians', 'Mumbai Indians')
]


CITY_CHOICES = [
    ('Bangalore', 'Bangalore'),
    ('Chandigarh', 'Chandigarh'),
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Kolkata', 'Kolkata'),
    ('Jaipur', 'Jaipur'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
    ('Cape Town', 'Cape Town'),
    ('Port Elizabeth', 'Port Elizabeth'),
    ('Durban', 'Durban'),
    ('Centurion', 'Centurion'),
    ('East London', 'East London'),
    ('Johannesburg', 'Johannesburg'),
    ('Kimberley', 'Kimberley'),
    ('Bloemfontein', 'Bloemfontein'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Cuttack', 'Cuttack'),
    ('Nagpur', 'Nagpur'),
    ('Dharamsala', 'Dharamsala'),
    ('Visakhapatnam', 'Visakhapatnam'),
    ('Pune', 'Pune'),
    ('Raipur', 'Raipur'),
    ('Ranchi', 'Ranchi'),
    ('Abu Dhabi', 'Abu Dhabi'),
    ('Sharjah', 'Sharjah'),
    ('Dubai', 'Dubai'),
    ('Rajkot', 'Rajkot'),
    ('Kanpur', 'Kanpur'),
    ('Bengaluru', 'Bengaluru'),
    ('Indore', 'Indore'),
    ('Navi Mumbai', 'Navi Mumbai'),
    ('Lucknow', 'Lucknow'),
    ('Guwahati', 'Guwahati'),
    ('Mohali', 'Mohali'),
]

class ProjectedScoreForm(forms.Form):
    batting_team = forms.ChoiceField(choices=TEAM_CHOICES, label="Batting Team")
    bowling_team = forms.ChoiceField(choices=TEAM_CHOICES, label="Bowling Team")
    city = forms.ChoiceField(choices=CITY_CHOICES, label="City")
    current_score = forms.IntegerField(label="Current Score")
    overs_done = forms.FloatField(label="Overs Completed (Works for overs > 5)")
    wickets_out = forms.IntegerField(label="Wickets Out")
    last_five_over = forms.IntegerField(label="Runs Scored in Last 5 Overs")

class WinPredictionForm(forms.Form):
    batting_team = forms.ChoiceField(choices=TEAM_CHOICES, label="Batting Team")
    bowling_team = forms.ChoiceField(choices=TEAM_CHOICES, label="Bowling Team")
    city = forms.ChoiceField(choices=CITY_CHOICES, label="City")
    target = forms.IntegerField(label="Target Score")
    current_score = forms.IntegerField(label="Current Score")
    overs_done = forms.FloatField(label="Overs Completed")
    wickets_out = forms.IntegerField(label="Wickets Out")
