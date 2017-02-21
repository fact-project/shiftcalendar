from .models import Role

LEGACY_SHIFTER = Role(
	name='legacy_shifter',
	title='the pre 2017 standard shifter')
LEGACY_EXPERT = Role(
	name='legacy_expert',
	title='the pre 2017 standard expert')
FALLBACK_SHIFTER = Role(
	name='fallback_shifter',
	title="gets all calls in case the real real shifter doesn't react")
SHIFTER_ON_CALL = Role(
	name='shifter_on_call',
	title='recieves calls in the middle of the night')
STARTER = Role(
	name='starter',
	title='performs the startup')
STOPPER = Role(
	name='stopper',
	title='performs the shutdown')

