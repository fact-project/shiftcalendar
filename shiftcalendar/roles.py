from .models import Role

LEGACY_SHIFTER = Role(
	name='shifter',
	title='pre 2017 standard shifter',
	color="DarkRed"
	)
LEGACY_EXPERT = Role(
	name='debug_shift',
	title='pre 2017 standard debug shift',
	color="Green",
	)
FALLBACK_SHIFTER = Role(
	name='fallback_shifter',
	title="gets all calls in case the real real shifter doesn't react",
	color="Red",
	)
SHIFTER_ON_CALL = Role(
	name='shifter_on_call',
	title='recieves calls in the middle of the night',
	color="LightSeaGreen",
	)
STARTER = Role(
	name='starter',
	title='performs the startup',
	color='DarkOrange',
	)
STOPPER = Role(
	name='stopper',
	title='performs the shutdown',
	color='PaleGreen',
	)

