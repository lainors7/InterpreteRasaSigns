## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## animation path
 * animation
    - utter_animation
    - action_animation

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* animation
    - utter_animation
    - action_animation

## interactive_story_1
* animation
    - utter_animation
    - action_animation
* greet
    - utter_greet
* animation
    - utter_animation
    - action_animation
* animation
    - utter_animation
    - action_animation
* animation
    - utter_animation
    - action_animation
* animation
    - utter_animation
    - action_animation
* animation
    - utter_animation
    - action_animation
