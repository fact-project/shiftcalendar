from .models import Role

LEGACY_SHIFTER = Role(
	name='legacy_shifter',
	title='the pre 2017 standard shifter',
	color="DarkRed"
	)
LEGACY_EXPERT = Role(
	name='legacy_expert',
	title='the pre 2017 standard expert',
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

