from peewee import *

from .database import logbook_db

class BaseModel(Model):
    class Meta:
        database = logbook_db

class Adminlog(BaseModel):
    action = CharField()
    data = TextField()
    dateline = BigIntegerField()
    ipaddress = CharField()
    module = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'adminlog'
        indexes = (
            (('module', 'action'), False),
        )

class Adminoptions(BaseModel):
    codepress = IntegerField()
    cpstyle = CharField()
    defaultviews = TextField()
    loginattempts = IntegerField()
    loginlockoutexpiry = IntegerField()
    notes = TextField()
    permissions = TextField()
    uid = PrimaryKeyField()

    class Meta:
        db_table = 'adminoptions'

class Adminsessions(BaseModel):
    data = TextField()
    dateline = BigIntegerField()
    ip = CharField()
    lastactive = BigIntegerField()
    loginkey = CharField()
    sid = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'adminsessions'

class Adminviews(BaseModel):
    conditions = TextField()
    custom_profile_fields = TextField()
    fields = TextField()
    perpage = IntegerField()
    sortby = CharField()
    sortorder = CharField()
    title = CharField()
    type = CharField()
    uid = IntegerField()
    vid = PrimaryKeyField()
    view_type = CharField()
    visibility = IntegerField()

    class Meta:
        db_table = 'adminviews'

class Announcements(BaseModel):
    aid = PrimaryKeyField()
    allowhtml = IntegerField()
    allowmycode = IntegerField()
    allowsmilies = IntegerField()
    enddate = BigIntegerField()
    fid = IntegerField(index=True)
    message = TextField()
    startdate = BigIntegerField()
    subject = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'announcements'

class Attachments(BaseModel):
    aid = PrimaryKeyField()
    attachname = CharField()
    dateuploaded = BigIntegerField()
    downloads = IntegerField()
    filename = CharField()
    filesize = IntegerField()
    filetype = CharField()
    pid = IntegerField()
    posthash = CharField(index=True)
    thumbnail = CharField()
    uid = IntegerField(index=True)
    visible = IntegerField()

    class Meta:
        db_table = 'attachments'
        indexes = (
            (('pid', 'visible'), False),
        )

class Attachtypes(BaseModel):
    atid = PrimaryKeyField()
    extension = CharField()
    icon = CharField()
    maxsize = IntegerField()
    mimetype = CharField()
    name = CharField()

    class Meta:
        db_table = 'attachtypes'

class Awaitingactivation(BaseModel):
    aid = PrimaryKeyField()
    code = CharField()
    dateline = BigIntegerField()
    misc = CharField()
    oldgroup = BigIntegerField()
    type = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'awaitingactivation'

class BackupAttachments(BaseModel):
    aid = PrimaryKeyField()
    attachname = CharField()
    dateuploaded = BigIntegerField()
    downloads = IntegerField()
    filename = CharField()
    filesize = IntegerField()
    filetype = CharField()
    pid = IntegerField()
    posthash = CharField(index=True)
    thumbnail = CharField()
    uid = IntegerField(index=True)
    visible = IntegerField()

    class Meta:
        db_table = 'backup_attachments'
        indexes = (
            (('pid', 'visible'), False),
        )

class BackupPolls(BaseModel):
    closed = IntegerField()
    dateline = BigIntegerField()
    multiple = IntegerField()
    numoptions = IntegerField()
    numvotes = IntegerField()
    options = TextField()
    pid = PrimaryKeyField()
    public = IntegerField()
    question = CharField()
    tid = IntegerField()
    timeout = BigIntegerField()
    votes = TextField()

    class Meta:
        db_table = 'backup_polls'

class BackupPollvotes(BaseModel):
    dateline = BigIntegerField()
    pid = IntegerField()
    uid = IntegerField()
    vid = PrimaryKeyField()
    voteoption = IntegerField()

    class Meta:
        db_table = 'backup_pollvotes'
        indexes = (
            (('pid', 'uid'), False),
        )

class BackupPosts(BaseModel):
    dateline = BigIntegerField(index=True)
    edittime = IntegerField()
    edituid = IntegerField()
    fid = IntegerField()
    icon = IntegerField()
    includesig = IntegerField()
    ipaddress = CharField()
    longipaddress = IntegerField(index=True)
    message = TextField(index=True)
    mobile = IntegerField()
    pid = PrimaryKeyField()
    posthash = CharField()
    replyto = IntegerField()
    smilieoff = IntegerField()
    subject = CharField()
    tid = IntegerField()
    uid = IntegerField(index=True)
    username = CharField()
    visible = IntegerField(index=True)

    class Meta:
        db_table = 'backup_posts'
        indexes = (
            (('tid', 'uid'), False),
        )

class BackupThreads(BaseModel):
    assign = IntegerField()
    assignuid = IntegerField()
    attachmentcount = IntegerField()
    bestanswer = IntegerField()
    closed = CharField()
    dateline = BigIntegerField(index=True)
    deletetime = IntegerField()
    fid = IntegerField()
    firstpost = IntegerField(index=True)
    icon = IntegerField()
    lastpost = BigIntegerField()
    lastposter = CharField()
    lastposteruid = IntegerField()
    mobile = IntegerField()
    notes = TextField()
    numratings = IntegerField()
    poll = IntegerField()
    prefix = IntegerField()
    priority = IntegerField()
    replies = IntegerField()
    status = IntegerField()
    statustime = IntegerField()
    statusuid = IntegerField()
    sticky = IntegerField()
    subject = CharField(index=True)
    tid = PrimaryKeyField()
    totalratings = IntegerField()
    uid = IntegerField(index=True)
    unapprovedposts = IntegerField()
    username = CharField()
    views = IntegerField()
    visible = IntegerField()

    class Meta:
        db_table = 'backup_threads'
        indexes = (
            (('fid', 'visible', 'sticky'), False),
            (('lastpost', 'fid'), False),
        )

class BackupThreadsubscriptions(BaseModel):
    dateline = BigIntegerField()
    notification = IntegerField()
    sid = PrimaryKeyField()
    subscriptionkey = CharField()
    tid = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'backup_threadsubscriptions'
        indexes = (
            (('tid', 'notification'), False),
        )

class Badwords(BaseModel):
    badword = CharField()
    bid = PrimaryKeyField()
    replacement = CharField()

    class Meta:
        db_table = 'badwords'

class Banfilters(BaseModel):
    dateline = BigIntegerField()
    fid = PrimaryKeyField()
    filter = CharField()
    lastuse = BigIntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'banfilters'

class Banned(BaseModel):
    admin = IntegerField()
    bantime = CharField()
    dateline = BigIntegerField(index=True)
    gid = IntegerField()
    lifted = BigIntegerField()
    oldadditionalgroups = TextField()
    olddisplaygroup = IntegerField()
    oldgroup = IntegerField()
    reason = CharField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'banned'

class Calendarpermissions(BaseModel):
    canaddevents = IntegerField()
    canbypasseventmod = IntegerField()
    canmoderateevents = IntegerField()
    canviewcalendar = IntegerField()
    cid = IntegerField()
    gid = IntegerField()

    class Meta:
        db_table = 'calendarpermissions'

class Calendars(BaseModel):
    allowhtml = IntegerField()
    allowimgcode = IntegerField()
    allowmycode = IntegerField()
    allowsmilies = IntegerField()
    allowvideocode = IntegerField()
    cid = PrimaryKeyField()
    disporder = IntegerField()
    eventlimit = IntegerField()
    moderation = IntegerField()
    name = CharField()
    showbirthdays = IntegerField()
    startofweek = IntegerField()

    class Meta:
        db_table = 'calendars'

class Captcha(BaseModel):
    dateline = BigIntegerField(index=True)
    imagehash = CharField(index=True)
    imagestring = CharField()

    class Meta:
        db_table = 'captcha'

class Datacache(BaseModel):
    cache = TextField()
    title = CharField(primary_key=True)

    class Meta:
        db_table = 'datacache'

class Delayedmoderation(BaseModel):
    dateline = BigIntegerField()
    delaydateline = BigIntegerField()
    did = PrimaryKeyField()
    fid = IntegerField()
    inputs = TextField()
    tids = TextField()
    type = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'delayedmoderation'

class Events(BaseModel):
    cid = IntegerField()
    dateline = IntegerField()
    description = TextField()
    eid = PrimaryKeyField()
    endtime = IntegerField()
    ignoretimezone = IntegerField()
    name = CharField()
    private = IntegerField(index=True)
    repeats = TextField()
    starttime = IntegerField()
    tid = IntegerField()
    timezone = CharField()
    uid = IntegerField()
    usingtime = IntegerField()
    visible = IntegerField()

    class Meta:
        db_table = 'events'
        indexes = (
            (('starttime', 'endtime'), False),
        )

class Forumpermissions(BaseModel):
    candeleteposts = IntegerField()
    candeletethreads = IntegerField()
    candlattachments = IntegerField()
    caneditattachments = IntegerField()
    caneditposts = IntegerField()
    canonlyviewownthreads = IntegerField()
    canpostattachments = IntegerField()
    canpostpolls = IntegerField()
    canpostreplys = IntegerField()
    canpostthreads = IntegerField()
    canratethreads = IntegerField()
    cansearch = IntegerField()
    canview = IntegerField()
    canviewthreads = IntegerField()
    canvotepolls = IntegerField()
    fid = IntegerField()
    gid = IntegerField()
    pid = PrimaryKeyField()

    class Meta:
        db_table = 'forumpermissions'

class Forums(BaseModel):
    active = IntegerField()
    allowavatars = IntegerField()
    allowhtml = IntegerField()
    allowimgcode = IntegerField()
    allowmycode = IntegerField()
    allowpicons = IntegerField()
    allowpostreps = IntegerField()
    allowsignatures = IntegerField()
    allowsmilies = IntegerField()
    allowtratings = IntegerField()
    allowvideocode = IntegerField()
    defaultdatecut = IntegerField()
    defaultsortby = CharField()
    defaultsortorder = CharField()
    description = TextField()
    disporder = IntegerField()
    fid = PrimaryKeyField()
    lastpost = IntegerField()
    lastposter = CharField()
    lastposteruid = IntegerField()
    lastpostsubject = CharField()
    lastposttid = IntegerField()
    linkto = CharField()
    mod_edit_posts = IntegerField()
    modattachments = IntegerField()
    modposts = IntegerField()
    modthreads = IntegerField()
    mysupport = IntegerField()
    mysupportmove = IntegerField()
    name = CharField()
    open = IntegerField()
    overridestyle = IntegerField()
    parentlist = TextField()
    password = CharField()
    pid = IntegerField()
    posts = IntegerField()
    rules = TextField()
    rulestitle = CharField()
    rulestype = IntegerField()
    showinjump = IntegerField()
    status = IntegerField()
    style = IntegerField()
    threads = IntegerField()
    type = CharField()
    unapprovedposts = IntegerField()
    unapprovedthreads = IntegerField()
    usepostcounts = IntegerField()
    usequickreply = IntegerField()

    class Meta:
        db_table = 'forums'

class Forumsread(BaseModel):
    dateline = IntegerField(index=True)
    fid = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'forumsread'
        indexes = (
            (('fid', 'uid'), True),
        )

class Forumsubscriptions(BaseModel):
    fid = IntegerField()
    fsid = PrimaryKeyField()
    uid = IntegerField()

    class Meta:
        db_table = 'forumsubscriptions'

class Groupleaders(BaseModel):
    canmanagemembers = IntegerField()
    canmanagerequests = IntegerField()
    gid = IntegerField()
    lid = PrimaryKeyField()
    uid = IntegerField()

    class Meta:
        db_table = 'groupleaders'

class Helpdocs(BaseModel):
    description = TextField()
    disporder = IntegerField()
    document = TextField()
    enabled = IntegerField()
    hid = PrimaryKeyField()
    name = CharField()
    sid = IntegerField()
    usetranslation = IntegerField()

    class Meta:
        db_table = 'helpdocs'

class Helpsections(BaseModel):
    description = TextField()
    disporder = IntegerField()
    enabled = IntegerField()
    name = CharField()
    sid = PrimaryKeyField()
    usetranslation = IntegerField()

    class Meta:
        db_table = 'helpsections'

class Icons(BaseModel):
    iid = PrimaryKeyField()
    name = CharField()
    path = CharField()

    class Meta:
        db_table = 'icons'

class Joinrequests(BaseModel):
    dateline = BigIntegerField()
    gid = IntegerField()
    reason = CharField()
    rid = PrimaryKeyField()
    uid = IntegerField()

    class Meta:
        db_table = 'joinrequests'

class Mailerrors(BaseModel):
    dateline = BigIntegerField()
    eid = PrimaryKeyField()
    error = TextField()
    fromaddress = CharField()
    message = TextField()
    smtpcode = IntegerField()
    smtperror = CharField()
    subject = CharField()
    toaddress = CharField()

    class Meta:
        db_table = 'mailerrors'

class Maillogs(BaseModel):
    dateline = BigIntegerField()
    fromemail = CharField()
    fromuid = IntegerField()
    ipaddress = CharField()
    message = TextField()
    mid = PrimaryKeyField()
    subject = CharField()
    tid = IntegerField()
    toemail = CharField()
    touid = BigIntegerField()

    class Meta:
        db_table = 'maillogs'

class Mailqueue(BaseModel):
    headers = TextField()
    mailfrom = CharField()
    mailto = CharField()
    message = TextField()
    mid = PrimaryKeyField()
    subject = CharField()

    class Meta:
        db_table = 'mailqueue'

class Massemails(BaseModel):
    conditions = TextField()
    dateline = BigIntegerField()
    format = IntegerField()
    htmlmessage = TextField()
    message = TextField()
    mid = PrimaryKeyField()
    perpage = IntegerField()
    senddate = BigIntegerField()
    sentcount = IntegerField()
    status = IntegerField()
    subject = CharField()
    totalcount = IntegerField()
    type = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'massemails'

class Mathbbcode(BaseModel):
    default = IntegerField()
    name = CharField()
    sid = PrimaryKeyField()
    url = CharField()

    class Meta:
        db_table = 'mathbbcode'

class Moderatorlog(BaseModel):
    action = TextField()
    data = TextField()
    dateline = BigIntegerField()
    fid = IntegerField()
    ipaddress = CharField()
    pid = IntegerField()
    tid = IntegerField(index=True)
    uid = IntegerField()

    class Meta:
        db_table = 'moderatorlog'

class Moderators(BaseModel):
    candeleteposts = IntegerField()
    caneditposts = IntegerField()
    canmanagethreads = IntegerField()
    canmovetononmodforum = IntegerField()
    canopenclosethreads = IntegerField()
    canviewips = IntegerField()
    fid = IntegerField()
    id = IntegerField()
    isgroup = IntegerField()
    mid = PrimaryKeyField()

    class Meta:
        db_table = 'moderators'
        indexes = (
            (('id', 'fid'), False),
        )

class Modtools(BaseModel):
    description = TextField()
    forums = TextField()
    name = CharField()
    postoptions = TextField()
    threadoptions = TextField()
    tid = PrimaryKeyField()
    type = CharField()

    class Meta:
        db_table = 'modtools'

class Mycode(BaseModel):
    active = IntegerField()
    cid = PrimaryKeyField()
    description = TextField()
    parseorder = IntegerField()
    regex = TextField()
    replacement = TextField()
    title = CharField()

    class Meta:
        db_table = 'mycode'

class Mysupport(BaseModel):
    description = CharField()
    extra = CharField()
    mid = PrimaryKeyField()
    name = CharField()
    type = CharField()

    class Meta:
        db_table = 'mysupport'

class Pages(BaseModel):
    dateline = BigIntegerField()
    enabled = IntegerField()
    framework = IntegerField()
    name = CharField()
    online = IntegerField()
    pid = PrimaryKeyField()
    template = TextField()
    url = CharField(unique=True)

    class Meta:
        db_table = 'pages'

class Polls(BaseModel):
    closed = IntegerField()
    dateline = BigIntegerField()
    multiple = IntegerField()
    numoptions = IntegerField()
    numvotes = IntegerField()
    options = TextField()
    pid = PrimaryKeyField()
    public = IntegerField()
    question = CharField()
    tid = IntegerField()
    timeout = BigIntegerField()
    votes = TextField()

    class Meta:
        db_table = 'polls'

class Pollvotes(BaseModel):
    dateline = BigIntegerField()
    pid = IntegerField()
    uid = IntegerField()
    vid = PrimaryKeyField()
    voteoption = IntegerField()

    class Meta:
        db_table = 'pollvotes'
        indexes = (
            (('pid', 'uid'), False),
        )

class Posts(BaseModel):
    dateline = BigIntegerField(index=True)
    edittime = IntegerField()
    edituid = IntegerField()
    fid = IntegerField()
    icon = IntegerField()
    includesig = IntegerField()
    ipaddress = CharField()
    longipaddress = IntegerField(index=True)
    message = TextField(index=True)
    mobile = IntegerField()
    pid = PrimaryKeyField()
    posthash = CharField()
    replyto = IntegerField()
    smilieoff = IntegerField()
    subject = CharField()
    tid = IntegerField()
    uid = IntegerField(index=True)
    username = CharField()
    visible = IntegerField(index=True)

    class Meta:
        db_table = 'posts'
        indexes = (
            (('tid', 'uid'), False),
        )

class Privatemessages(BaseModel):
    dateline = BigIntegerField()
    deletetime = BigIntegerField()
    folder = IntegerField()
    fromid = IntegerField()
    icon = IntegerField()
    includesig = IntegerField()
    message = TextField()
    pmid = PrimaryKeyField()
    readtime = BigIntegerField()
    receipt = IntegerField()
    recipients = TextField()
    smilieoff = IntegerField()
    status = IntegerField()
    statustime = BigIntegerField()
    subject = CharField()
    toid = IntegerField(index=True)
    uid = IntegerField()

    class Meta:
        db_table = 'privatemessages'
        indexes = (
            (('uid', 'folder'), False),
        )

class Profilefields(BaseModel):
    description = TextField()
    disporder = IntegerField()
    editable = IntegerField()
    fid = PrimaryKeyField()
    hidden = IntegerField()
    length = IntegerField()
    maxlength = IntegerField()
    name = CharField()
    postnum = BigIntegerField()
    required = IntegerField()
    type = TextField()

    class Meta:
        db_table = 'profilefields'

class Promotionlogs(BaseModel):
    dateline = BigIntegerField()
    newusergroup = IntegerField()
    oldusergroup = CharField()
    pid = IntegerField()
    plid = PrimaryKeyField()
    type = CharField()
    uid = IntegerField()

    class Meta:
        db_table = 'promotionlogs'

class Promotions(BaseModel):
    description = TextField()
    enabled = IntegerField()
    logging = IntegerField()
    newusergroup = IntegerField()
    originalusergroup = CharField()
    pid = PrimaryKeyField()
    posts = IntegerField()
    posttype = CharField()
    referrals = IntegerField()
    referralstype = CharField()
    registered = IntegerField()
    registeredtype = CharField()
    reputations = IntegerField()
    reputationtype = CharField()
    requirements = CharField()
    title = CharField()
    usergrouptype = CharField()

    class Meta:
        db_table = 'promotions'

class Reportedposts(BaseModel):
    dateline = BigIntegerField(index=True)
    fid = IntegerField(index=True)
    pid = IntegerField()
    reason = CharField()
    reportstatus = IntegerField()
    rid = PrimaryKeyField()
    tid = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'reportedposts'

class Reputation(BaseModel):
    adduid = IntegerField()
    comments = TextField()
    dateline = BigIntegerField(index=True)
    pid = IntegerField(index=True)
    reputation = BigIntegerField()
    rid = PrimaryKeyField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'reputation'

class Searchlog(BaseModel):
    dateline = BigIntegerField()
    ipaddress = CharField()
    keywords = TextField()
    posts = TextField()
    querycache = TextField()
    resulttype = CharField()
    sid = CharField(primary_key=True)
    threads = TextField()
    uid = IntegerField()

    class Meta:
        db_table = 'searchlog'

class Sessions(BaseModel):
    anonymous = IntegerField()
    ip = CharField(index=True)
    location = CharField()
    location1 = IntegerField(index=True)
    location2 = IntegerField(index=True)
    nopermission = IntegerField()
    sid = CharField(primary_key=True)
    time = BigIntegerField(index=True)
    uid = IntegerField(index=True)
    useragent = CharField()

    class Meta:
        db_table = 'sessions'

class Settinggroups(BaseModel):
    description = TextField()
    disporder = IntegerField()
    gid = PrimaryKeyField()
    isdefault = IntegerField()
    name = CharField()
    title = CharField()

    class Meta:
        db_table = 'settinggroups'

class Settings(BaseModel):
    description = TextField()
    disporder = IntegerField()
    gid = IntegerField()
    isdefault = IntegerField()
    name = CharField()
    optionscode = TextField()
    sid = PrimaryKeyField()
    title = CharField()
    value = TextField()

    class Meta:
        db_table = 'settings'

class Smilies(BaseModel):
    disporder = IntegerField()
    find = CharField()
    image = CharField()
    name = CharField()
    showclickable = IntegerField()
    sid = PrimaryKeyField()

    class Meta:
        db_table = 'smilies'

class Spiders(BaseModel):
    language = CharField()
    lastvisit = BigIntegerField()
    name = CharField()
    sid = PrimaryKeyField()
    theme = IntegerField()
    useragent = CharField()
    usergroup = IntegerField()

    class Meta:
        db_table = 'spiders'

class Stats(BaseModel):
    dateline = BigIntegerField(primary_key=True)
    numposts = IntegerField()
    numthreads = IntegerField()
    numusers = IntegerField()

    class Meta:
        db_table = 'stats'

class Tasklog(BaseModel):
    data = TextField()
    dateline = BigIntegerField()
    lid = PrimaryKeyField()
    tid = IntegerField()

    class Meta:
        db_table = 'tasklog'

class Tasks(BaseModel):
    day = CharField()
    description = TextField()
    enabled = IntegerField()
    file = CharField()
    hour = CharField()
    lastrun = BigIntegerField()
    locked = BigIntegerField()
    logging = IntegerField()
    minute = CharField()
    month = CharField()
    nextrun = BigIntegerField()
    tid = PrimaryKeyField()
    title = CharField()
    weekday = CharField()

    class Meta:
        db_table = 'tasks'

class Templategroups(BaseModel):
    gid = PrimaryKeyField()
    prefix = CharField()
    title = CharField()

    class Meta:
        db_table = 'templategroups'

class Templates(BaseModel):
    dateline = IntegerField()
    sid = IntegerField()
    status = CharField()
    template = TextField()
    tid = PrimaryKeyField()
    title = CharField()
    version = CharField()

    class Meta:
        db_table = 'templates'

class Templatesets(BaseModel):
    sid = PrimaryKeyField()
    title = CharField()

    class Meta:
        db_table = 'templatesets'

class Themes(BaseModel):
    allowedgroups = TextField()
    def_ = IntegerField(db_column='def')
    name = CharField()
    pid = IntegerField()
    properties = TextField()
    stylesheets = TextField()
    tid = PrimaryKeyField()
    wysiwyg_theme = CharField()

    class Meta:
        db_table = 'themes'

class Themestylesheets(BaseModel):
    attachedto = TextField()
    cachefile = CharField()
    lastmodified = BigIntegerField()
    name = CharField()
    sid = PrimaryKeyField()
    stylesheet = TextField()
    tid = IntegerField()

    class Meta:
        db_table = 'themestylesheets'

class Threadprefixes(BaseModel):
    displaystyle = CharField()
    forums = TextField()
    groups = TextField()
    pid = PrimaryKeyField()
    prefix = CharField()

    class Meta:
        db_table = 'threadprefixes'

class Threadratings(BaseModel):
    ipaddress = CharField()
    rating = IntegerField()
    rid = PrimaryKeyField()
    tid = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'threadratings'
        indexes = (
            (('tid', 'uid'), False),
        )

class Threads(BaseModel):
    assign = IntegerField()
    assignuid = IntegerField()
    attachmentcount = IntegerField()
    bestanswer = IntegerField()
    closed = CharField()
    dateline = BigIntegerField(index=True)
    deletetime = IntegerField()
    fid = IntegerField()
    firstpost = IntegerField(index=True)
    icon = IntegerField()
    lastpost = BigIntegerField()
    lastposter = CharField()
    lastposteruid = IntegerField()
    mobile = IntegerField()
    notes = TextField()
    numratings = IntegerField()
    poll = IntegerField()
    prefix = IntegerField()
    priority = IntegerField()
    replies = IntegerField()
    status = IntegerField()
    statustime = IntegerField()
    statusuid = IntegerField()
    sticky = IntegerField()
    subject = CharField(index=True)
    tid = PrimaryKeyField()
    totalratings = IntegerField()
    uid = IntegerField(index=True)
    unapprovedposts = IntegerField()
    username = CharField()
    views = IntegerField()
    visible = IntegerField()

    class Meta:
        db_table = 'threads'
        indexes = (
            (('fid', 'visible', 'sticky'), False),
            (('lastpost', 'fid'), False),
        )

class Threadsread(BaseModel):
    dateline = IntegerField(index=True)
    tid = IntegerField()
    uid = IntegerField()

    class Meta:
        db_table = 'threadsread'
        indexes = (
            (('tid', 'uid'), True),
        )

class Threadsubscriptions(BaseModel):
    dateline = BigIntegerField()
    notification = IntegerField()
    sid = PrimaryKeyField()
    subscriptionkey = CharField()
    tid = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        db_table = 'threadsubscriptions'
        indexes = (
            (('tid', 'notification'), False),
        )

class Threadviews(BaseModel):
    tid = IntegerField(index=True)

    class Meta:
        db_table = 'threadviews'

class UpgradeData(BaseModel):
    contents = TextField()
    title = CharField(unique=True)

    class Meta:
        db_table = 'upgrade_data'

class Userfields(BaseModel):
    fid1 = TextField()
    fid3 = TextField()
    fid4 = TextField(null=True)
    fid5 = TextField(null=True)
    fid6 = TextField(null=True)
    fid7 = TextField(null=True)
    fid8 = TextField(null=True)
    fid9 = TextField(null=True)
    ufid = PrimaryKeyField()

    class Meta:
        db_table = 'userfields'

class Usergroups(BaseModel):
    attachquota = BigIntegerField()
    canaddevents = IntegerField()
    canassign = IntegerField()
    canbeassigned = IntegerField()
    canbypasseventmod = IntegerField()
    canchangename = IntegerField()
    cancp = IntegerField()
    cancustomtitle = IntegerField()
    candeleteposts = IntegerField()
    candeletethreads = IntegerField()
    candenypmreceipts = IntegerField()
    candisplaygroup = IntegerField()
    candlattachments = IntegerField()
    caneditattachments = IntegerField()
    caneditposts = IntegerField()
    cangivereputations = IntegerField()
    canmanagesupportdenial = IntegerField()
    canmarksolved = IntegerField()
    canmarktechnical = IntegerField()
    canmodcp = IntegerField()
    canmoderateevents = IntegerField()
    canoverridepm = IntegerField()
    canpostattachments = IntegerField()
    canpostpolls = IntegerField()
    canpostreplys = IntegerField()
    canpostthreads = IntegerField()
    canratemembers = IntegerField()
    canratethreads = IntegerField()
    canreceivewarnings = IntegerField()
    cansearch = IntegerField()
    canseepriorities = IntegerField()
    canseetechnotice = IntegerField()
    cansendemail = IntegerField()
    cansendpms = IntegerField()
    cansetpriorities = IntegerField()
    cantrackpms = IntegerField()
    canundovotes = IntegerField()
    canuploadavatars = IntegerField()
    canusepms = IntegerField()
    canusercp = IntegerField()
    canusesig = IntegerField()
    canusesigxposts = BigIntegerField()
    canview = IntegerField()
    canviewcalendar = IntegerField()
    canviewmemberlist = IntegerField()
    canviewonline = IntegerField()
    canviewonlineips = IntegerField()
    canviewprofiles = IntegerField()
    canviewthreads = IntegerField()
    canviewwolinvis = IntegerField()
    canvotepolls = IntegerField()
    canwarnusers = IntegerField()
    description = TextField()
    disporder = IntegerField()
    gid = PrimaryKeyField()
    image = CharField()
    isbannedgroup = IntegerField()
    issupermod = IntegerField()
    maxemails = IntegerField()
    maxpmrecipients = IntegerField()
    maxreputationsday = BigIntegerField()
    maxreputationsperthread = BigIntegerField()
    maxreputationsperuser = BigIntegerField()
    maxwarningsday = IntegerField()
    namestyle = CharField()
    pmquota = IntegerField()
    reputationpower = BigIntegerField()
    showforumteam = IntegerField()
    showinbirthdaylist = IntegerField()
    signofollow = IntegerField()
    starimage = CharField()
    stars = IntegerField()
    title = CharField()
    type = IntegerField()
    usereputationsystem = IntegerField()
    usertitle = CharField()

    class Meta:
        db_table = 'usergroups'

class Users(BaseModel):
    additionalgroups = CharField()
    aim = CharField()
    allownotices = IntegerField()
    avatar = CharField()
    avatardimensions = CharField()
    avatartype = CharField()
    away = IntegerField()
    awaydate = IntegerField()
    awayreason = CharField()
    birthday = CharField(index=True)
    birthdayprivacy = CharField()
    buddylist = TextField()
    classicpostbit = IntegerField()
    coppauser = IntegerField()
    dateformat = CharField()
    daysprune = IntegerField()
    deniedsupport = IntegerField()
    deniedsupportreason = IntegerField()
    deniedsupportuid = IntegerField()
    displaygroup = IntegerField()
    dst = IntegerField()
    dstcorrection = IntegerField()
    email = CharField()
    failedlogin = BigIntegerField()
    hideemail = IntegerField()
    icq = CharField()
    ignorelist = TextField()
    invisible = IntegerField()
    language = CharField()
    lastactive = BigIntegerField()
    lastip = CharField()
    lastpost = BigIntegerField()
    lastvisit = BigIntegerField()
    loginattempts = IntegerField()
    loginkey = CharField()
    longlastip = IntegerField(index=True)
    longregip = IntegerField(index=True)
    moderateposts = IntegerField()
    moderationtime = BigIntegerField()
    msn = CharField()
    mysupportdisplayastext = IntegerField()
    notepad = TextField()
    password = CharField()
    pmfolders = TextField()
    pmnotice = IntegerField()
    pmnotify = IntegerField()
    postnum = IntegerField()
    ppp = IntegerField()
    receivefrombuddy = IntegerField()
    receivepms = IntegerField()
    referrals = IntegerField()
    referrer = IntegerField()
    regdate = BigIntegerField()
    regip = CharField()
    reputation = BigIntegerField()
    returndate = CharField()
    salt = CharField()
    showavatars = IntegerField()
    showcodebuttons = IntegerField()
    showquickreply = IntegerField()
    showredirect = IntegerField()
    showsigs = IntegerField()
    signature = TextField()
    style = IntegerField()
    subscriptionmethod = IntegerField()
    suspendposting = IntegerField()
    suspendsignature = IntegerField()
    suspendsigtime = BigIntegerField()
    suspensiontime = BigIntegerField()
    threadmode = CharField()
    timeformat = CharField()
    timeonline = BigIntegerField()
    timezone = CharField()
    totalpms = IntegerField()
    tpp = IntegerField()
    uid = PrimaryKeyField()
    unreadpms = IntegerField()
    usemobileversion = IntegerField()
    usergroup = IntegerField(index=True)
    username = CharField(unique=True)
    usernotes = TextField()
    usertitle = CharField()
    warningpoints = IntegerField()
    website = CharField()
    yahoo = CharField()

    class Meta:
        db_table = 'users'

class Usertitles(BaseModel):
    posts = IntegerField()
    starimage = CharField()
    stars = IntegerField()
    title = CharField()
    utid = PrimaryKeyField()

    class Meta:
        db_table = 'usertitles'

class Warninglevels(BaseModel):
    action = TextField()
    lid = PrimaryKeyField()
    percentage = IntegerField()

    class Meta:
        db_table = 'warninglevels'

class Warnings(BaseModel):
    dateline = BigIntegerField()
    daterevoked = BigIntegerField()
    expired = IntegerField()
    expires = BigIntegerField()
    issuedby = IntegerField()
    notes = TextField()
    pid = IntegerField()
    points = IntegerField()
    revokedby = IntegerField()
    revokereason = TextField()
    tid = IntegerField()
    title = CharField()
    uid = IntegerField()
    wid = PrimaryKeyField()

    class Meta:
        db_table = 'warnings'

class Warningtypes(BaseModel):
    expirationtime = BigIntegerField()
    points = IntegerField()
    tid = PrimaryKeyField()
    title = CharField()

    class Meta:
        db_table = 'warningtypes'

