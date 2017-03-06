$(document).ready(function() {
    var role_color = {};
    var username = {};
    var rolename = {};
    $.ajax({
      url: '/usernames',
      dataType: "json",
      success: function(json) {
        json.forEach(function(val, index){
          username[val.user_id] = val.username;
        });
      },
    });

    $.ajax({
      url: '/roles',
      dataType: "json",
      success: function(json) {
        json.forEach(function(val, index){
          role_color[val.id] = val.color;
          rolename[val.id] = val.name;
        });
      },
    });

    // DN: this is shit! should maybe come from DB, or ... idk
    var role_start_offsets = {
      5: moment.duration(18, 'hours'),  // 5: starter: 18h - 22h
      4: moment.duration(22, 'hours'),  // 4: shifter on call: 22h - 6am  (8 hours)
      6: moment.duration(6, 'hours'),  // 6: stopper: 6h am - 8h am (next day)
    };
    var role_default_durations = {
      5: moment.duration(4, 'hours'),
      6: moment.duration(2, 'hours'),
      4: moment.duration(8, 'hours'),
    };

    var user_id_choice = "";
    var role_id_choice = "";

    $("#username").change(function() {
      user_id_choice = $(this).val();
    });

    $("#role").change(function() {
      role_id_choice = $(this).val();
    });

    var calendar = $('#calendar').fullCalendar({

    views: {
      agenda: {
        // options apply to basicWeek and agendaWeek views
        slotDuration: "01:00:00",
        minTime: "00:00:00",
        maxTime: "1.00:00:00",
        allDayText: "all night",
      },
    },

    editable: true,
    defaultTimedEventDuration: "06:00:00",
    forceEventDuration: true,
    events: "/events",
    selectable: true,
    selectHelper: true,

    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month'
    },

    eventDataTransform: function( event ) {
      event.color = role_color[event.role_id];
      return event;
    },

    eventRender:
    function (event, element, view) {
        $(element).tooltip({title: rolename[event.role_id]});
        $(element).find('.fc-event').addClass(event.className.join(' '));
    },


    select: function(start, end) {
      if (user_id_choice) {
        var start_str;
        var end_str;
        if (role_id_choice in role_start_offsets)
        {
          for (days = 0; days < end.diff(start, 'days'); days+=1)
          {
            start_str = moment(start)
              .add(days, 'days')
              .add(role_start_offsets[role_id_choice])
              .format("YYYY-MM-DD HH:mm:ss");
            end_str = moment(start)
              .add(days, 'days')
              .add(role_start_offsets[role_id_choice])
              .add(role_default_durations[role_id_choice])
              .format("YYYY-MM-DD HH:mm:ss");
            $.ajax({
              url: '/add_events',
              data: {
                  user_id: user_id_choice,
                  role_id: role_id_choice ,
                  start: start_str,
                  end: end_str,
              },
              type: "POST",
            });
          }
        }
        else {
          start_str = start.format("YYYY-MM-DD HH:mm:ss");
          end_str = end.format("YYYY-MM-DD HH:mm:ss");
          $.ajax({
            url: '/add_events',
            data: {
              user_id: user_id_choice,
              role_id: role_id_choice ,
              start: start_str,
              end: end_str,
            },
            type: "POST",
          });
        }
        calendar.fullCalendar('unselect');
        calendar.fullCalendar('refetchEvents');
      }
    },

    eventDrop: function(event, delta) {
      var start = event.start.format()
      var end = event.end.format();
      $.ajax({
        url: '/update_events',
        data: 'start='+ start +'&end='+ end +'&id='+ event.id ,
        type: "POST",
      });
    },

    eventResize: function(event) {
      var start = event.start.format();
      var end = event.end.format();
      $.ajax({
        url: '/update_events',
        data: 'start='+ start +'&end='+ end +'&id='+ event.id ,
        type: "POST",
      });
    },

    eventClick: function(event) {
      if (confirm("Would you like to delete this?")) {
        $.ajax({
          type: "POST",
          url: "/delete_event",
          data: "id=" + event.id
        });
        calendar.fullCalendar('removeEvents', event.id);
      }
      return false;
    },
  });
});
