import React from 'react';

const Projects = () => {
  return (
    <section id="projects" className="section projects">
      <h2>My Projects</h2>
      <div className="project-list">
        <div className="project-card">
          <h3>Hand tracking algorithm</h3>
          <p> 
  Developed a hand gesture recognition system.
  Used OpenCV, Python and Mediapipe 
  Has the functionality to  control video playback
  Has play/pause functionality as well as seek forward/backward. 
  Added on-screen gesture confirmation using thumbs-up detection to reduce false triggers.
</p>
        </div>
        <div className="project-card">
          <h3>Youtube Video downloader</h3>
          <p> 
Created an application using python to download any youtube video.
Included the option to choose between MP3 and MP4 format.
Added the option to  choose the video quality of the MP4 download.
</p>
        </div>
      </div>
    </section>
  );
};

export default Projects;
