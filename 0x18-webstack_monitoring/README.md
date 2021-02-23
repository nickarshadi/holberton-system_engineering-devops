

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="Holberton School">
    <meta name="google" content="notranslate">

    <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <title>Project: 0x18. Webstack monitoring | Holberton Intranet</title>

    <link rel="stylesheet" media="all" href="/assets/application_coral-2b0154c7f8f09927f5dbe62a6d91b8a3e988c6d320d1564dd17402e8bbeec5e3.css" />
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="/assets/application-de3338c37d1f030f4e3fe62014125863b651bc44b16e5a0135827a4617930759.js"></script>
    <link rel="shortcut icon" type="image/x-icon" href="/favicon_coral.ico" />
    <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="LGHRyPtB2Rlt2MPrEYFc0hjDQWMTFIslI3SaaqJs2qpjUcsOITRahj5Xuhive3P7JMa4w/5icCTlmphUQqbVmA==" />

    <link rel="apple-touch-icon" href="/apple-touch-icon_coral.png">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Video player -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/ewwink/clappr-quality-selector-plugin@latest/quality-selector.js"></script>

    <!-- Store user timezone -->
    <script>
      Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
    </script>

    <script src="/packs/js/application-e76d55f6e9e4cb094e0a.js"></script>
  </head>

  <body class="
    signed_in
    env_production
    
    "
    translate="no"
    class="notranslate"
    data-theme-suffix="_coral"
    data-checker-special-theme="">

      <input type="hidden" id="hbtn-slack-url" value="https://holberton-students.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
      <span class="name">Holberton</span>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i class="fa fa-info-circle"></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i class="fa fa-calendar"></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Projects"><a href="/dashboards/my_current_projects"><div class="icon "><i class="fa fa-code-fork"></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Professional track"><a href="/dashboards/my_professional_track"><div class="icon "><i class="fa fa-thumbs-o-up"></i></div><div class="visible-xs">Professional track</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews"><a href="/dashboards/corrections_i_can_make"><div class="icon "><i class="fa fa-check"></i></div><div class="visible-xs">QA Reviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i class="fa fa-commenting-o"></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i class="fa fa-question"></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i class="fa fa-graduation-cap"></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Concepts"><a href="/dashboards/my_concepts"><div class="icon "><i class="fa fa-file-text"></i></div><div class="visible-xs">Concepts</div></a></li>
    
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i class="fa fa-video-camera"></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/dashboards/my_server"><div class="icon "><i class="fa fa-server"></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Sandboxes"><a href="/dashboards/my_containers"><div class="icon "><i class="fa fa-terminal"></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i class="fa fa-wrench"></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/dashboards/my_peers"><div class="icon "><i class="fa fa-users"></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i class="fa fa-book"></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i class="fa fa-building"></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i class="fa fa-microphone"></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-students.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/001/477/thumb/gMfADJp0_400x400.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210218T213155Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4b72e5a155166bf9b0aebf1cd458032f43f9c54566c86bf2661f24988e196318')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i class="fa fa-info-circle"></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i class="fa fa-calendar"></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Projects"><a href="/dashboards/my_current_projects"><div class="icon "><i class="fa fa-code-fork"></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Professional track"><a href="/dashboards/my_professional_track"><div class="icon "><i class="fa fa-thumbs-o-up"></i></div><div class="visible-xs">Professional track</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews"><a href="/dashboards/corrections_i_can_make"><div class="icon "><i class="fa fa-check"></i></div><div class="visible-xs">QA Reviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i class="fa fa-commenting-o"></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i class="fa fa-question"></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i class="fa fa-graduation-cap"></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Concepts"><a href="/dashboards/my_concepts"><div class="icon "><i class="fa fa-file-text"></i></div><div class="visible-xs">Concepts</div></a></li>
    
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i class="fa fa-video-camera"></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/dashboards/my_server"><div class="icon "><i class="fa fa-server"></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Sandboxes"><a href="/dashboards/my_containers"><div class="icon "><i class="fa fa-terminal"></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i class="fa fa-wrench"></i></div><div class="visible-xs">Tools</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/dashboards/my_peers"><div class="icon "><i class="fa fa-users"></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i class="fa fa-book"></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i class="fa fa-building"></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i class="fa fa-microphone"></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton-students.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/001/477/thumb/gMfADJp0_400x400.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210218T213155Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4b72e5a155166bf9b0aebf1cd458032f43f9c54566c86bf2661f24988e196318')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
      <div id="layout-bars">
        

        

        

        

          <a
    class="onair-container "
    data-target="#video_streams_current_modal"
    data-toggle="modal"
    href="#"
    title="Video Streaming in progress...">
    <div class="icon-container">
      <i class="fa fa-television" aria-hidden="true"></i>
      <i class="fa fa-podcast animate-flicker" aria-hidden="true"></i>
    </div>

    Watch the live stream
  </a>

      </div>

      <article class="">
        

  <div id="jigsaw-shortcut-lists">



</div>


<h1 class="gap">0x18. Webstack monitoring</h1>


<div id="project_id" style="display: none" data-project-id="281"></div>

<p class="sm-gap">
  <small>
    <i class="fa fa-folder-open"></i>
    Foundations - System engineering &amp; DevOps  Web stack
  </small>
</p>


  <p>
    <em>
      <small>
        <i class="fa fa-user"></i> By Sylvain Kalache, co-founder at Holberton School
      </small>
    </em>
  </p>




  <p>
    <small>
      <i class="fa fa-calendar"></i>
          Ongoing project - started 02-17-2021, must end by 02-19-2021 (in about 7 hours)
        - you're done with <span id="student_task_done_percentage">0</span>% of tasks.
    </small>
  </p>

    <p>
      <small>
        <i class="fa fa-check"></i>
          Checker was released at 02-18-2021 07:12 AM
      </small>
    </p>


    <p>
      <small>
        <i class="fa fa-check-square"></i>
        QA review fully automated.
      </small>
    </p>








    <div class="gap formatted-content">
      <p style="margin-bottom: 0"><em>For this project, students are expected to look at these concepts:</em></p>
      <ul style="margin-top: 5px">
          <li>
            <em><a href="/concepts/13">Monitoring</a></em>
          </li>
          <li>
            <em><a href="/concepts/67">Server</a></em>
          </li>
      </ul>
    </div>

  <article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png" alt="" style="" /></p>

<h2>Background Context</h2>

<p>&ldquo;You cannot fix or improve what you cannot measure&rdquo; is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.</p>

<p>Web stack monitoring can be broken down into 2 categories:</p>

<ul>
<li>Application monitoring: getting data about your running software and making sure it is behaving as expected</li>
<li>Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)</li>
</ul>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg" alt="" style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/m8e7smqRz3k4PUBnv0zB7g" title="What is server monitoring" target="_blank">What is server monitoring</a> </li>
<li><a href="/rltoken/fGzCCVr7lwNEvarE8u1HRQ" title="What is application monitoring" target="_blank">What is application monitoring</a> </li>
<li><a href="/rltoken/h6WV2iIVUCL-atjFIu6TZA" title="System monitoring by Google" target="_blank">System monitoring by Google</a> </li>
<li><a href="/rltoken/ZUIlnid6NphRWIaGZ3MTZQ" title="Nginx logging and monitoring" target="_blank">Nginx logging and monitoring</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/HjJQMilktjdS5BksAfLY0Q" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why is monitoring needed</li>
<li>What are the 2 main area of monitoring</li>
<li>What are access logs for a web server (such as Nginx)</li>
<li>What are error logs for a web server (such as Nginx)</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

  </article>




    <!-- Servers -->
      <hr class="gap">
      <h2 class="gap">Your servers</h2>

      <table class="table table-striped">
    <thead>
        <tr>
        <th>Name</th>
        <th>Username</th>
        <th>IP</th>
        <th>State</th>
            <th colspan="3"></th>
        </tr>
    </thead>

    <tbody>
            <tr>
                <td>1477-web-01</td>
                <td><code>ubuntu</code></td>
                <td><code>35.227.13.38</code></td>
                <td>running</td>
                <td>
                        <a data-confirm="Are you sure to reboot 1477-web-01?" href="/servers/4181/soft_reboot">Soft reboot</a>
                </td>
                    <td><a data-confirm="Are you sure to hard reboot 1477-web-01?" href="/servers/4181/hard_reboot">Hard reboot</a></td>
                <td>
                        <span style="color: #FF0000; font-weight: 600;">Last: </span>
                    <a data-confirm="Are you sure you&#39;d like a new server?
- This server will be destroyed
- Did you update your public SSH key in your user profile yet?

This action can take time...
Please, be patient..." href="/servers/4181/ask_new">Ask a new server</a>
                </td>
            </tr>
            <tr>
                <td>1477-web-02</td>
                <td><code>ubuntu</code></td>
                <td><code>35.231.175.126</code></td>
                <td>running</td>
                <td>
                        <a data-confirm="Are you sure to reboot 1477-web-02?" href="/servers/4438/soft_reboot">Soft reboot</a>
                </td>
                    <td><a data-confirm="Are you sure to hard reboot 1477-web-02?" href="/servers/4438/hard_reboot">Hard reboot</a></td>
                <td>
                        <span style="color: #FF0000; font-weight: 600;">Last: </span>
                    <a data-confirm="Are you sure you&#39;d like a new server?
- This server will be destroyed
- Did you update your public SSH key in your user profile yet?

This action can take time...
Please, be patient..." href="/servers/4438/ask_new">Ask a new server</a>
                </td>
            </tr>
            <tr>
                <td>1477-lb-01</td>
                <td><code>ubuntu</code></td>
                <td><code>34.74.174.156</code></td>
                <td>running</td>
                <td>
                        <a data-confirm="Are you sure to reboot 1477-lb-01?" href="/servers/4439/soft_reboot">Soft reboot</a>
                </td>
                    <td><a data-confirm="Are you sure to hard reboot 1477-lb-01?" href="/servers/4439/hard_reboot">Hard reboot</a></td>
                <td>
                        <span style="color: #FF0000; font-weight: 600;">Last: </span>
                    <a data-confirm="Are you sure you&#39;d like a new server?
- This server will be destroyed
- Did you update your public SSH key in your user profile yet?

This action can take time...
Please, be patient..." href="/servers/4439/ask_new">Ask a new server</a>
                </td>
            </tr>
    </tbody>
</table>


    <!-- Tasks -->
      <hr class="gap">
      <h2 class="gap">Tasks</h2>
      <section class="formatted-content">
            <div data-role="task3936" data-position="1">
              <div class=" clearfix gap" id="task-3936">
<span id="user_id" data-id="1477"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="3936">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="3936" data-project-id="281" data-toggle="modal" data-target="#task-3936-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-3936-users-done-modal" data-task-id="3936" data-project-id="281">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Sign up for Datadog and install datadog-agent"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    0. Sign up for Datadog and install datadog-agent
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>For this task head to <a href="/rltoken/Uho9kxbX9KHCSYAQ-Zl1AQ" title="https://www.datadoghq.com/" target="_blank">https://www.datadoghq.com/</a> and sign up for a free <code>Datadog</code> account. When signing up, you&rsquo;ll have the option of selecting statistics from your current stack that <code>Datadog</code> can monitor for you. Once you have an account set up, follow the instructions given on the website to install the <code>Datadog</code> agent. </p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T213155Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=68fec393f6fc11cab0224fc61a975723f05d9c11fda6a6a7f765222f79a62cac" alt="" style="" /></p>

<ul>
<li>Sign up for Datadog - <strong>Please make sure you are using the US website of Datagog (.com)</strong></li>
<li>Install <code>datadog-agent</code> on <code>web-01</code></li>
<li>Create an <code>application key</code></li>
<li>Copy-paste in your Intranet user profile (<a href="/rltoken/2D6j3Y6G9c8o_t278-Cu_w" title="here" target="_blank">here</a>) your DataDog <code>API key</code>  and your DataDog <code>application key</code>.</li>
<li>Your server <code>web-01</code> should be visible in Datadog under the host name <code>XX-web-01</code>

<ul>
<li>You can validate it by using this <a href="/rltoken/CyrSkrD0zPWXK4YBRRbTvw" title="API" target="_blank">API</a></li>
<li>If needed, you will need to update the hostname of your server</li>
</ul></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x18-webstack_monitoring</code></li>
    </ul>


    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="3936" data-toggle="modal" data-target="#task-3936-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-3936-whiteboard-modal" data-task-id="3936">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "0. Sign up for Datadog and install datadog-agent"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="3936" data-toggle="modal" data-target="#task-test-correction-3936-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-3936-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. Sign up for Datadog and install datadog-agent"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="3936">Start a new test</button>
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>
                <div class="help">
                    <button data-task-id="3936">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="3936">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



      <!-- Button containers -->
        <button class="task_containers_modal btn btn-default size_three" data-task-id="3936" data-container-spec-ids="[19, 21]" data-toggle="modal" data-target="#task-containers-3936-modal">
          Get a sandbox
        </button>
        <div class="modal fade task_containers_modal" id="task-containers-3936-modal" data-task-id="3936" data-container-spec-ids="[19, 21]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Sandboxes</h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available 8 months max</p>

        <div class="panel panel-default" id="task_3936_container_spec_19">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3936" data-container-spec-id="19">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3936" data-container-spec-id="19">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel panel-default" id="task_3936_container_spec_21">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04 - Python 3.5 / Fabric / Puppet</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3936" data-container-spec-id="21">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3936" data-container-spec-id="21">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap">
            <b>URL? Private IP? Public IP?</b><br>
            If a <b>URL</b> is provided, you can use it from anywhere.<br>
            If no <b>URL</b> is provided, you must use the <b>private IP</b> when you are at school. From outside, you must use the <b>public IP</b>.
            <br><br>
            <b>Ports mapping</b><br>
            Each exposed port is mapped to another one. Example: the port SSH <code>22</code> is mapped to the port <code>33511</code>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


      <!-- Button for QA Review -->
    </div>

</div>

            </div>
            <div data-role="task3942" data-position="2">
              <div class=" clearfix gap" id="task-3942">
<span id="user_id" data-id="1477"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="3942">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="3942" data-project-id="281" data-toggle="modal" data-target="#task-3942-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-3942-users-done-modal" data-task-id="3942" data-project-id="281">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Monitor some metrics"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    1. Monitor some metrics
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some <code>monitors</code> within the <code>Datadog</code> dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: <a href="/rltoken/naY47nur2yPJNw8tdACnzQ" title="System Check" target="_blank">System Check</a>.</p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T213155Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9fd5d42966fd45dfcf92a2521ecdbfbdfe1c8766b9b552d1ccb0742604ecce2e" alt="" style="" /></p>

<ul>
<li>Set up a monitor that checks the number of read requests issued to the device per second.</li>
<li>Set up a monitor that checks the number of write requests issued to the device per second.</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x18-webstack_monitoring</code></li>
    </ul>


    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="3942" data-toggle="modal" data-target="#task-3942-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-3942-whiteboard-modal" data-task-id="3942">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "1. Monitor some metrics"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="3942" data-toggle="modal" data-target="#task-test-correction-3942-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-3942-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Monitor some metrics"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="3942">Start a new test</button>
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>
                <div class="help">
                    <button data-task-id="3942">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="3942">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



      <!-- Button containers -->
        <button class="task_containers_modal btn btn-default size_three" data-task-id="3942" data-container-spec-ids="[19, 21]" data-toggle="modal" data-target="#task-containers-3942-modal">
          Get a sandbox
        </button>
        <div class="modal fade task_containers_modal" id="task-containers-3942-modal" data-task-id="3942" data-container-spec-ids="[19, 21]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Sandboxes</h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available 8 months max</p>

        <div class="panel panel-default" id="task_3942_container_spec_19">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3942" data-container-spec-id="19">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3942" data-container-spec-id="19">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel panel-default" id="task_3942_container_spec_21">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04 - Python 3.5 / Fabric / Puppet</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3942" data-container-spec-id="21">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3942" data-container-spec-id="21">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap">
            <b>URL? Private IP? Public IP?</b><br>
            If a <b>URL</b> is provided, you can use it from anywhere.<br>
            If no <b>URL</b> is provided, you must use the <b>private IP</b> when you are at school. From outside, you must use the <b>public IP</b>.
            <br><br>
            <b>Ports mapping</b><br>
            Each exposed port is mapped to another one. Example: the port SSH <code>22</code> is mapped to the port <code>33511</code>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


      <!-- Button for QA Review -->
    </div>

</div>

            </div>
            <div data-role="task3943" data-position="3">
              <div class=" clearfix gap" id="task-3943">
<span id="user_id" data-id="1477"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="3943">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="3943" data-project-id="281" data-toggle="modal" data-target="#task-3943-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-3943-users-done-modal" data-task-id="3943" data-project-id="281">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Create a dashboard"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    2. Create a dashboard
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Now create a dashboard with different metrics displayed in order to get a few different visualizations.</p>

<ul>
<li>Create a new <code>dashboard</code></li>
<li>Add at least 4 <code>widgets</code> to your dashboard. They can be of any type and monitor whatever you&rsquo;d like</li>
<li>Create the answer file <code>2-setup_datadog</code> which has the <code>dashboard_id</code> on the first line. <strong>Note</strong>: in order to get the id of your dashboard, you may need to use <a href="/rltoken/VrzQP39UUFMmAKZx0IZLuw" title="Datadog&#39;s API" target="_blank">Datadog&rsquo;s API</a></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x18-webstack_monitoring</code></li>
        <li>File: <code>2-setup_datadog</code></li>
    </ul>


    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="3943" data-toggle="modal" data-target="#task-3943-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-3943-whiteboard-modal" data-task-id="3943">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "2. Create a dashboard"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="3943" data-toggle="modal" data-target="#task-test-correction-3943-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-3943-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Create a dashboard"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="3943">Start a new test</button>
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                    </center>
                </div>
                <div class="result"></div>
                <div class="help">
                    <button data-task-id="3943">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="3943">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check-circle" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-times-circle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



      <!-- Button containers -->
        <button class="task_containers_modal btn btn-default size_three" data-task-id="3943" data-container-spec-ids="[19, 21]" data-toggle="modal" data-target="#task-containers-3943-modal">
          Get a sandbox
        </button>
        <div class="modal fade task_containers_modal" id="task-containers-3943-modal" data-task-id="3943" data-container-spec-ids="[19, 21]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Sandboxes</h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available 8 months max</p>

        <div class="panel panel-default" id="task_3943_container_spec_19">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3943" data-container-spec-id="19">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3943" data-container-spec-id="19">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel panel-default" id="task_3943_container_spec_21">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 16.04 - Python 3.5 / Fabric / Puppet</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="3943" data-container-spec-id="21">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="3943" data-container-spec-id="21">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap">
            <b>URL? Private IP? Public IP?</b><br>
            If a <b>URL</b> is provided, you can use it from anywhere.<br>
            If no <b>URL</b> is provided, you must use the <b>private IP</b> when you are at school. From outside, you must use the <b>public IP</b>.
            <br><br>
            <b>Ports mapping</b><br>
            Each exposed port is mapped to another one. Example: the port SSH <code>22</code> is mapped to the port <code>33511</code>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


      <!-- Button for QA Review -->
    </div>

</div>

            </div>
      </section>











      </article>

      <div class="copyright">Copyright &copy; 2021 Holberton School. All rights reserved.</div>
    </main>

      <div id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
    <i class="fa fa-search" aria-hidden="true"></i>
    <i class="fa fa-window-minimize" aria-hidden="true"></i>
</div>

      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="Start search by typing in this field">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>

        <div class="modal fade" id="video_streams_current_modal">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Video streaming</h4>
            </div>
            <div class="modal-body">
                <ul class="streams list-group"></ul>
                <div class="player">
                    <div class="header">
                        <div class="back"><i class="fa fa-chevron-left" aria-hidden="true"></i></div>
                        <div class="title"></div>
                    </div>
                    <div id="video_streams_current_modal_player"></div>
                </div>
                <div class="spinner">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="error"></div>
            </div>
        </div>
    </div>
</div>



      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '1477'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>



      <input id="checker_pride_assets" type="hidden" value="[]">

      
  </body>
</html>

