import {Component, OnInit, Input} from '@angular/core';
import {ActivityDTO} from "../../model/activity.dto";
import {CandidateDTO} from "../../model/candidate.dto";

@Component({
  selector: 'candidate-activities',
  template: `
    
    <div class="left-pane">
      <div class="candidate-details">
        <img class="singing-man-icon" src="../../../assets/images/avatar.png" />
          <div class="candidate-name">{{candidate.candidateName}}</div>
          <div class="seperator"></div>
      <div >
      <div class="candidate-score">{{candidate.averageScore | number : '1.2-2'}}</div>
      <div>Average Score</div>
      </div>
      <div class="seperator"></div>
      <div class="team-average-score">{{candidate.teamAverageScore | number : '1.2-2'}}</div>
      <div>Team Average Score</div>
                  
      </div>      
    </div>
    <div class="center-pane">      
      <div class="activities-list">        
        <div class="activity-details" *ngFor="let activity of candidateActivities">
          <h5>{{activity.songName}}</h5>
          <span >Score: {{activity.activityAvgScore}}</span>
           <span>|</span>
          <span>Date: {{activity.datePerformed}}</span>
        </div>
      </div>
    </div>
    
`,
  styleUrls: ['candidate-activities.component.css']
})

export class CandidateActivitiesComponent implements OnInit {

  @Input() candidateActivities:ActivityDTO;
  @Input() candidate: CandidateDTO;

  constructor() { }

  ngOnInit() {
    console.log(this.candidateActivities)
  }

}

