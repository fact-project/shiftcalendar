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
      var role_id_choice = $("#role_select").val();
      var user_id_choice = $("#username_select").val();
      if (user_id_choice) {
        alert("before ajax call");
        $.ajax({
              url: '/add_events',
              data: {
                  user_id: user_id_choice,
                  role_id: role_id_choice ,
                  start: start.format("YYYY-MM-DD HH:mm:ss"),
                  end: end.format("YYYY-MM-DD HH:mm:ss"),
              },
              type: "POST",
            });
        calendar.fullCalendar('unselect');
        calendar.fullCalendar('refetchEvents');
      }
    },

    eventDrop: function(event, delta) {
      var start = event.start.format();
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
