## Enroll Course Story
* greet
  - utter_greet
* user_wants_to_enroll
  - utter_display_programs
* user_choose_program
  - action_display_course
* user_choose_course
  - action_display_course_info
* user_choose_save_seat
  - utter_save_seat
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
  - action_email_admission_depart
  - action_email_admitted_student
  - utter_goto_home
* user_choose_home
  - utter_greet


## College information Story
* greet
  - utter_greet
* user_wants_college_info
  - utter_display_college_info
  - utter_goto_home
* user_choose_home
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

<!-- ## form Testing path
* network_issue
  - form_info
  - form{"name": "form_info"}
  - form{"name": null} -->


## College Facilites
* greet
  - utter_greet
* user_choose_campuslife
  - action_display_facilities
* user_choose_any_facility
  - action_display_facility_info
  - utter_goto_home
* user_choose_home
  - utter_greet
