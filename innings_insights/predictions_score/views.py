from django.shortcuts import render
import pickle
import pandas as pd
from .forms import ProjectedScoreForm, WinPredictionForm


with open('D://InningsInsights(Python Individual)//innings_insights//pkl//projected_score.pkl', 'rb') as f:
    projected_score_model = pickle.load(f)

with open('D://InningsInsights(Python Individual)//innings_insights//pkl//win_prediction.pkl', 'rb') as f:
    win_prediction_model = pickle.load(f)

def home(request):
    return render(request, 'home.html')  # Create a home.html template

def projected_score(request):
    teams = [
        'Royal Challengers Bengaluru',
        'Gujarat Titans',
        'Lucknow Super Giants',
        'Punjab Kings',
        'Delhi Capitals',
        'Sunrisers Hyderabad',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Kolkata Knight Riders',
        'Mumbai Indians'
    ]
    cities = [
        'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
        'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
        'Centurion', 'East London', 'Johannesburg', 'Kimberley',
        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
        'Sharjah', 'Dubai', 'Rajkot', 'Kanpur', 'Bengaluru', 'Indore',
        'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali'
    ]
    if request.method == 'POST':
        form = ProjectedScoreForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            batting_team = form.cleaned_data['batting_team']
            bowling_team = form.cleaned_data['bowling_team']
            city = form.cleaned_data['city']
            current_score = form.cleaned_data['current_score']
            overs = form.cleaned_data['overs_done']
            wickets = form.cleaned_data['wickets_out']
            last_five = form.cleaned_data['last_five_over']

            # Calculate required fields
            balls_left = 120 - (overs * 6)
            wickets_left = 10 - wickets
            crr = current_score / overs

            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [city],
                'current_score': [current_score],
                'balls_left': [balls_left],
                'wickets_left': [wickets_left],
                'current_run_rate': [crr],
                'last_five_over': [last_five]
            })

            # Predict using model
            result = projected_score_model.predict(input_df)
            predicted_score = int(result[0])
            return render(request, 'projected_score.html', {'form': form, 'predicted_score': predicted_score, 
                                                            'teams': teams, 'cities': cities})
        else:
            print(form.errors)

    else:
        form = ProjectedScoreForm()

    return render(request, 'projected_score.html', {'form': form, 'teams': teams, 'cities': cities})

def win_prediction(request):
    teams = [
        'Royal Challengers Bengaluru',
        'Gujarat Titans',
        'Lucknow Super Giants',
        'Punjab Kings',
        'Delhi Capitals',
        'Sunrisers Hyderabad',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Kolkata Knight Riders',
        'Mumbai Indians'
    ]
    cities = [
        'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
        'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
        'Centurion', 'East London', 'Johannesburg', 'Kimberley',
        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
        'Sharjah', 'Dubai', 'Rajkot', 'Kanpur', 'Bengaluru', 'Indore',
        'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali'
    ]
    if request.method == 'POST':
        form = WinPredictionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            batting_team = form.cleaned_data['batting_team']
            bowling_team = form.cleaned_data['bowling_team']
            city = form.cleaned_data['city']
            target = form.cleaned_data['target']
            current_score = form.cleaned_data['current_score']
            overs = form.cleaned_data['overs_done']
            wickets = form.cleaned_data['wickets_out']

            # Calculate required fields
            runs_left = target - current_score
            balls_left = 120 - (overs * 6)
            wickets_left = 10 - wickets
            crr = current_score / overs if overs != 0 else 0
            rrr = (runs_left * 6) / balls_left if balls_left != 0 else float('inf')

            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets_left': [wickets_left],
                'total_runs_x': [target],
                'current_run_rate': [crr],
                'required_run_rate': [rrr]
            })

            # Predict using model
            result = win_prediction_model.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]

            return render(request, 'win_prediction.html', {'form': form,'win': round(win * 100), 'loss': round(loss * 100),
                                                           'teams': teams, 'cities': cities})
        else:
            print(form.errors)

    else:
        form = WinPredictionForm()

    return render(request, 'win_prediction.html', {'form': form, 'teams': teams, 'cities': cities})