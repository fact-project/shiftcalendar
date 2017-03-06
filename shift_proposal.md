
# FACT SSP shifts

This document contains a proposal on how to organize FACT shifts in the age of automatization. The goal is to minimize manpower spent during night time while maintaining a high amount of observation time without jeopardizing the detector.

While in 'shifter awake' mode, the long winter nights are problematic (because too long shift duration), in 'shifter on call' mode the short summer nights are problematic: since start and park need human supervision (for safety reasons), the time between start and park results in a very short period the shifter has a chance to sleep.

Taking into account that some people tend to stay awake until late every evening, while others tend to wake up early every morning, it seems possible that such 'late' and 'early birds' can take 'start' and 'park' duties without too much disturbing their normal life.

| evening | night | morning | day |
| --- | --- | --- | ---
| Starter | Shifter | Parker | -none- |
| Fallback shifter | FBS | FBS | FBS |
| Flare expert | FE | FE | FE |
| Fallback Flare expert | FBFE | FBFE | FBFE |
| Shifthelper exception (hardcoded!) | SE | SE | SE |
| Expert | Expert |  Expert | Expert |


# Role Duties:

Below the duties involved in the different shifts are stated.

## ​Starter

- The Starters shift begins around civil twilight in the evening.
- The duty of the starter is to perform the main.js task named "Startup", observe data taking for 10 minutes and submit the startup-checklist.
  - This task should be performed under acceptable (tbd) weather conditions. Neither rain nor reasonable wind can harm FACT, since the camera is water tight and in observation position, the window is facing away from any rain or hail. Depending on the weather, an automatic procedure (tbd) shall decide all night about stopping/resuming observation.
  - In case of heavy storm (tbd) however, no start-up is performed. In this case the starter ticks the "No observation possible" box in the checklist and makes sure the system is not switched on. No Shifter will be called during the night under this conditions. The Parker however is still asked to check the status of FACT  in the morning. In case a heavy storm moved FACT, there might still be time to call for help before the sun rises.
- After filling and submitting the checklist, the Starters shift is over. The SH knows that the Shifter has to take over now.

## ​Shifter

- The shifters shift begins after the Startup has been done. The shifters duty is to be available on the phone under all circumstances. This involves taking care of not entering areas with bad signal reception. He has to make sure to have a list of expert contacts available, not relying on webpages.
- Upon being called by the shifthelper, the shifter deals with the problem either himself or by calling an Expert. Under all conditions every action has to be logged.
- The shifter may call an expert for any reason in case he feels unable to deal with a situation. If no expert can be reached or the expert advises, the shifter is allowed to stop datataking for the night. Such a decision must be written in the logbook, and an e-mail to fact-online has to be sent.
- The shifters shift ends automatically at the beginning of astronomical twilight of the next morning.
- Reasonable weather condions shall be handled by automatic suspend/resume. In case of very strong storm, the shifter is called. In this case, he has to ensure the telescope is parked. After such a condition, no observation shall be resumed by the shifter.

## ​Parker

- The Parkers duty is to make sure FACT is parked before sun dawn.
- The Parker is called by the shifthelper in the morning, unless the Parker informs the SH that "I am awake". It is perfectly fine to use this call as an additional wake up call.
- The Parkers shift ends by submitting the shut down checklist.
- The Parker is responsible for writing the summary of the weather of the last night based on the overview video. [http://fact-project.org/overview\_video/](http://fact-project.org/overview_video/)

## ​Fallback Shifter

- The Fallback Shifters Duty it is to be reachable all the time.
- In case the Fallback Shifter is called, something went bad with one of the shifters. Reasons for a call to the fallback shifter include:
  - starter, shifter or parker (SSP) are not reachable on their phone due to bad reception
  - SSP shift entries missing in the shift database.
  - SSP failed to acknowledge a shifthelper alert for 15 minutes.
  - SSP forgot how to reach help and use the SH to call for help.
- When the fallback shifter is called, the same actions shall be performed as SSP should have done. In addition, fallback shifter shall establish contact to the current SSP on duty and find out what is wrong.
- For the Fallback shifter to be contacted is an exceptional condition which is worth to be logged in the logbook. In addition, a mail shall be sent to the spokesperson.
- Shifters repeatedly causing calls to their fallbacks might be subject to penalties.

## Flare Expert

- The duty of the Flare Expert is to be reachable and receive automatic calls in case the system detected a source flaring state.
- The SH will initiate a call to the Flare Expert in case a flare flag has been set by a program provided by the Flare Experts.
- The SH will continue calling Flare Experts until the flare flag is reset in order not to miss any flare.

## ​Fallback Flare Expert

- The Fallback Flare Experts duty are identical to those of the Flare Expert.
- The Fallback Flare Expert is called if the flare flag has not been reset within XXX minutes.

## ​Shifthelper Exception (hardcoded)

- The duty of the Shifthelper Exception Shifter is to receive calls in case the SH itself is not working properly, or fallback shifters cannot be reached. Such events shall be reported in the logbook.
- Their numbers are hardcoded in the SH source code, so that DB failures cannot lead to them not being reachable.
- In case no shifter and no fallback shifter is reachable, the exception shifter is allowed to stop the operation for the night. An email to fact-online must be sent in such a case.
- Shifthelper Exceptions shifts **may overlap** with other shifts. So a person can be on Starter shift while being hard coded as "Shifthelper Exception".

## ​Experts

System experts are not directly contacted by the SH. They shall be reachable in case a shifter feels unsure about how to handle a situation. In case they also cannot solve the problem, they are allowed to instruct the shifter to stop the operation for the night.



# Technical Details of *planned* vs. *executed* shift times

As stated above, the Starter shifts ends, once the Startup checklist has been submitted.
So the Starter shifts (when planned) begins at civil twilight in the evening and goes on until the planned
beginning of the Parker shift, i.e. until one hour before dawn.
Only when the startup checklist is submitted the entry in the shiftcalendar is updated to end "now".
In order for the Starter to take all the time she needs to perform the startup
the startup shifts in its planned state takes the entire night.

The shifters shift in its planned state also takes the entire night, i.e. it starts at
civil twilight in the evening and spans until sundawn in the morning. So it starts at the
same time the starter shifts starts and it ends together with the Parker shift.
However the shifthelper will never call a shifter as long as it finds either at Starter
or a Parker on shift. This is encoded in the way to shifthelper finds out whom to call.
The shifters start or end times are not updated when the starter submits the startup checklist.
So how quickly or how slowly the Starter might work, as soon as the starter is not on shift anymore,
there is always a shifter on shift.
In this sense the shifters shift works as a security net, for errors leading to no starter or no
parker being on shift. (In addition to the fallback shifter)

The Parkers planned shift starts one hour before sun dawn and spans until the shutdown checklist has been submitted. Thus the parker can end her shift earler by submitting the checklist very quickly, but can not start the shift earlier.

There is a task to be solved here. At the moment, the shifthelper calls (St,Pa or Sh) when 20 minutes before shutdown nobody pressed the 'I am awake' button.
If the shutdown (be it on purpose or by chance) is scheduled in the middle of the night. This call will not reach the parker but the shifter. Since the Shift times are referenced to the sun, while the shutdown time can be any time. If this call is the result of the shutdown being mistakenly scheduled in the middle of the night, it is fine to wake the shifter. Might not be shifters fault, but its an error ... its night ... so shifter should deal with it.
When it was planned, well the plan was bad. People might want to plan the shutdown in the middle of the night, because at that point the moon becomes so bright that observations make no sense. The solution in this case is to schedule a "sleep" at the time one wants to schedule "shutdown" and put the "shutdown" at the time where it belongs. This must be clear to people planning to observe in moon nights.

The same should be taken into account when planning to perform technical measurements in moon nights.
If at all possible, schedule the startup around sunset, then schedule a "sleep" until the time is right for your technical measurement, and afterwars schedule a "sleep" until it is time to "shutdown" in the morning.
At the moment, there is no clean way to schedule technical measurements like this, but there might be in the future.


### User stories:

- The starter is done setting up the observation and submits the startup-checklist. This time the shifthelper needs to know to stop calling the starter and start calling the shifter instead. So there must be an entry in some kind of database made, once the checklist is submitted and there must be some kind of feedback for the starter to **see** that the shifthelper got the message and it is safe safe to assume the shifter is called from now on.

- The starter has problems getting the system running and at some point (1h?) his **planned** shift is over, so while he is still working on the system, the shifthelper switches over and starts calling the shifter, who is already sleeping. **Not good**. [This is already solved by the pseudo unlimited starter shift now.]

- The starter submitted the checklist and observes after a minute, there is still something wrong with the system. Now he wants to keep the system from waking up the shifter. So the starter should be able to "take back" the checklist submission, or in a sense "aquire responsibility" leading to an update in the shift DB again. In principle this may be also true for experts beeing called by shifters for help. Also they might want to "aquire responsibility" and thus make sure they are called instead of the shifter (or in addition to the shifter?). This would also make sure the intervention by an expert is kept track of so we can correctly reward them.

- Not to forget: people might become ill during the night and swap shifts on very short notice, e.g. a starter might also do the shifter shift since the shifter does not feel well at all. The system should not allow to alter shiftcalendar entries for days in the past in order to avoid people accidentally changing the wrong date.

- The problem is: when somebody cannot do his or her shift, because they are have no network access, and we do not allow people to change the shift calendar, then people cannot simply swap shifts. Also, we cannot keep track of who changed what and how in the shiftcalendar, so in case errors were made, we are screwed.
Why can we not keep track of who changed what? Well technically we can keep track of this.
This can be done e.g. by not storing what we want to **have** in the shiftcalendar, but what people want to **change** in the shiftcalendar. So instead of *updating* and entry changing e.g. the username, there will be a *new entry* essentially being a copy of the entry one wanted to change, just with a different username, in addition every entry will carry the time it was created and by whom it was created. This ensures we have the entire history of modifications made by people to the shiftcalendar. Getting the current state from this entire history is just a little more difficult now. And reverting changes made by somebody by accident is still not the easiest thing to do, but it is possible. Its just work.

If we fear, people might screw up the shiftcalendar all the time, because they can. We can of course forbid them to alter entries and just alow this to a handful of people. And in case somebody needs to swap shifts, they have to call (what ever time it might be) one of these people. Still these people might screw it up then, but obviously this is okay then, because these people are somehow special.

### Typical load per type

number of calls per week

| shift | mean | std | median |
| --- | --- | --- | ---
| Starter | 4 | 6 | 2 |
| Shifter | 23 | 30 | 16 |
| Parker | 12 | 12 | 9 |

16 calls per week for a sleeping shifter is a lot. However this
statistic includes calls to developers as well as "duplicate" calls, i.e. a call that is going out
5minutes or 2minutes after another call, so the shifter is not woken up twice.

The median time between two calls is with 2.2minutes fairly close to the minimum time of 2minutes, which shows how difficult it is to interpret these numbers.

