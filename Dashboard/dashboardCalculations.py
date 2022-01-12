import operator
import streamlit as st
import numpy as np
import plotly.express as px


# Preference calculation based on survey
def survey_pref_calc(goal, travel_kids, age, trip_duration, comfort_level, disability):
    totalprice = "Price"
    totalwaitingtimeinhours = "Total Waiting Time"
    totaltraveltimeinhours = "Total Travel Time"
    totalwalkingdistance = "Total Walking Distance"


    preference = {
        totalprice: 0,
        totalwaitingtimeinhours: 0,
        totaltraveltimeinhours: 0,
        totalwalkingdistance: 0,
    }

    if goal == "Leisure":
        preference[totalprice] += 0.6
        preference[totalwaitingtimeinhours] += 0.7
        preference[totaltraveltimeinhours] += 0.7
        preference[totalwalkingdistance] += 0.5

    elif goal == "Adventure":

        preference[totalprice] += 0.2
        preference[totalwaitingtimeinhours] += 0.7
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5

    elif goal == "Quality time with family":

        preference[totalprice] += 0.5
        preference[totalwaitingtimeinhours] += 0.8
        preference[totaltraveltimeinhours] += 0.8
        preference[totalwalkingdistance] += 1

    elif goal == "Learn about experience/culture":

        preference[totalprice] += 0.8
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5

    elif goal == "Daily business":

        preference[totalprice] += 0.7
        preference[totalwaitingtimeinhours] += 0.9
        preference[totaltraveltimeinhours] += 0.9
        preference[totalwalkingdistance] += 0.9

    elif goal == "Other":

        preference[totalprice] += 0.5
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5

    elif travel_kids == "Yes":
        preference[totalprice] += 0.5
        preference[totalwaitingtimeinhours] += 0.9
        preference[totaltraveltimeinhours] += 0.9
        preference[totalwalkingdistance] += 1

    elif travel_kids == "No":
        preference[totalprice] += 0.7
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5

    elif age == "16-25":

        preference[totalprice] += 0.9
        preference[totalwaitingtimeinhours] += 0.3
        preference[totaltraveltimeinhours] += 0.3
        preference[totalwalkingdistance] += 0.2

    elif age == "25-45":

        preference[totalprice] += 0.3
        preference[totalwaitingtimeinhours] += 0.8
        preference[totaltraveltimeinhours] += 0.8
        preference[totalwalkingdistance] += 0.4

    elif age == "45-65":

        preference[totalprice] += 0.3
        preference[totalwaitingtimeinhours] += 0.8
        preference[totaltraveltimeinhours] += 0.8
        preference[totalwalkingdistance] += 0.7

    elif age == ">65":

        preference[totalprice] += 0.6
        preference[totalwaitingtimeinhours] += 0.3
        preference[totaltraveltimeinhours] += 0.3
        preference[totalwalkingdistance] += 0.9

    elif age == "I do not want to tell":
        preference[totalprice] += 0.5
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5


    elif trip_duration == "<1":

        preference[totalprice] += 0.2
        preference[totalwaitingtimeinhours] += 0.9
        preference[totaltraveltimeinhours] += 0.9
        preference[totalwalkingdistance] += 0.9

    elif trip_duration == "1-3":
        preference[totalprice] += 0.4
        preference[totalwaitingtimeinhours] += 0.7
        preference[totaltraveltimeinhours] += 0.7
        preference[totalwalkingdistance] += 0.7

    elif trip_duration == ">3":
        preference[totalprice] += 0.6
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5

    elif comfort_level == "Comfort does not matter much to me (better cheaper)":

        preference[totalprice] += 0.2
        preference[totalwaitingtimeinhours] += 0.9
        preference[totaltraveltimeinhours] += 0.9
        preference[totalwalkingdistance] += 0.9

    elif comfort_level == "I am fine to be a bit uncomfortable during the trip":
        preference[totalprice] += 0.9
        preference[totalwaitingtimeinhours] += 0.2
        preference[totaltraveltimeinhours] += 0.2
        preference[totalwalkingdistance] += 0.2

    elif comfort_level == "I prefer to have full comfort (better faster)":
        preference[totalprice] += 0.9
        preference[totalwaitingtimeinhours] += 0.2
        preference[totaltraveltimeinhours] += 0.2
        preference[totalwalkingdistance] += 0.2

    elif disability == "Yes":
        preference[totalprice] += 0.2
        preference[totalwaitingtimeinhours] += 0.9
        preference[totaltraveltimeinhours] += 0.9
        preference[totalwalkingdistance] += 0.9

    elif disability == "No":
        preference[totalprice] += 0.9
        preference[totalwaitingtimeinhours] += 0.2
        preference[totaltraveltimeinhours] += 0.2
        preference[totalwalkingdistance] += 0.2

    elif disability == "I prefer not to answer":
        preference[totalprice] += 0.5
        preference[totalwaitingtimeinhours] += 0.5
        preference[totaltraveltimeinhours] += 0.5
        preference[totalwalkingdistance] += 0.5


    return max(preference.items(), key=operator.itemgetter(1))[0]


# Function for generating additional recommendations
def additional_recommendation(df, preference):
    minvalue = df[preference].min()

    threshold = 0.05

    additional_recommendation_df = df.loc[(df[preference] > minvalue) & (df[preference] <= (minvalue + threshold))]

    while additional_recommendation_df.empty:

        threshold += 0.05
        additional_recommendation_df = df.loc[(df[preference] > minvalue) & (df[preference] <= (minvalue + threshold))]
        if not additional_recommendation_df.empty:
            additional_recommendation_df.drop_duplicates(subset=["finalsolutionusedlabels"], inplace=True)
            st.write(f":information_source: When the __{preference}__ is __{additional_recommendation_df[preference].to_string(index=False)}__ units, the features of your trip and "
                     f"the transport you should choose are the next (Route 1 on the chart):")
            st.info(":minibus:" + "__" + additional_recommendation_df["finalsolutionusedlabels"].to_string(index=False).strip("[]") + "__")
            break
    return additional_recommendation_df


# TODO: make the feature name look nice
# Indicator showing the extent to which the search results change due to an adjustment of the filters
def indicator_calculation(feature, filterTuple, df_initial, df_filtered):
    increase_indicator = 5

    if df_initial[feature].max() > filterTuple[1] or df_initial[feature].min() < filterTuple[0]:

        if (len(df_initial.index) - len(df_filtered.index)) >= increase_indicator and (
                len(df_initial.index) - len(df_filtered.index)) < increase_indicator * 2:

            st.write(f"{feature} :arrow_up:")

        elif (len(df_initial.index) - len(df_filtered.index)) >= increase_indicator * 2 and (
                len(df_initial.index) - len(df_filtered.index)) < increase_indicator * 3:

            st.write(f"{feature} :arrow_up: :arrow_up:")
        elif (len(df_initial.index) - len(df_filtered.index)) >= increase_indicator * 3:
            st.write(f"{feature} :arrow_up: :arrow_up: :arrow_up:")

# Assigning unique ids to the rows
def assign_ids(df):
    df_with_ids = df.assign(
        id=(df['Total Walking Distance'].astype(str) + '_' + df[
            'Price'].astype(str)
            + '_' + df['Total Travel Time'].astype(str)
            + '_' + df['Total Waiting Time'].astype(str)
            + '_' + df['safety_boost'].astype(str)
            + '_' + df['caloriesBurnt_avg'].astype(str)
            + '_' + df['stresslevel'].astype(str)
            + '_' + df['mood_upgrade'].astype(str)
            + '_' + df['earnings_gross'].astype(str)
            + '_' + df['delay_probability'].astype(str)
            + '_' + df['multimodality'].astype(str)
            )
            .astype('category').cat.codes)
    df_with_ids['id'] = df_with_ids['id'].astype(np.int64)

    return df_with_ids


def draw_parallel_coord(df):

    st.write(df)
    return px.parallel_coordinates(
        df,
        color="id",
        labels={"id": "Route",
                "Price": "Price",
                "Total Walking Distance": "Walking Distance",
                "Total Travel Time": "Travel Time",
                "Total Waiting Time": "Waiting Time",
                "safety_boost": "Safety Degree",
                "earnings_gross": "Earnings",
                "caloriesBurnt_avg": "Calories Burnt",
                "delay_probability":"Delay Chance",
                "multimodality": "Transport Change"
                },
    )

# TODO: enhance with the Boolean filters
# Showing the indicators
def show_indicators(df_filtered, df, filters):

    for feature, filter1 in zip(df_filtered, filters):

        if df_filtered.dtypes[feature] == np.float64 or df_filtered.dtypes[
            feature] == np.int64:
            indicator_calculation(feature, filter1, df, df_filtered)

    # TODO: output it only when the indicator appears
    st.info("* 1 arrow = if you adjust this feature a few of additional recommendations appear \n"
            "* 2 arrows = if you adjust this feature a dozen of additional recommendations appear \n"
            "* 3 arrows = if you adjust this feature a lot of additional recommendations appear \n"
            "* Also, try to deselect all checkboxes  \n")


def check_amount_lines(df_filtered, amount_lines):
    if (len(df_filtered.index) > amount_lines):
        st.info("Looks complicated? Please try to filter your preferences a bit more.")

# def change_in_filter(filter_initial_upper_value, filter_initial_lower_value, filter_tuple):
#     if filter_initial_upper_value != filter_tuple[1] or filter_initial_lower_value != filter_tuple[0]:
#         st.write(filter_initial_upper_value)
#         st.write(filter_tuple[1])
#         return True
