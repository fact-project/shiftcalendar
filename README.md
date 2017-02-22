# FACT shift calendar website

This is a web front for shifters to check and modify their FACT night shifts.

It uses `fullcalendar.js` for rendering the calendar entries.
The Database backend is running on La Palma, see file `mysql_schema.sql` for details
on the tables.

php is used only on the serverside to execute the DB queries.
I deliberately kept the php parts short and stupid, because the language is crap
and error prone.

`login.php` is stolen from other FACT apps

## Deployment

in case you want to deploy this app. Be it on your laptop for testing or
on a new machine. You probably need to adapt this:

 * credentials: The credentials look like those in our (php credentials repo)[github.com/fact-project/php_credentials]
	So you need to clone that repo and adjust all `/home/dneise/sandbox_db.php`
	lines to point to the place where you cloned the credentials.
 * `this_url`: In all ajax calls in `index.html` I had to define the url
 	pointing to the place where the app is running.
 	So you'll have to adapt `this_url` to reflect that.

## Missing features:

 * usernames have to come from the Database!

## Auth:

I use simple OAuth against our LDAP server. This is not nice with sessions and all,
but its secure enough and I have no clue of sessions and all that stuff.

