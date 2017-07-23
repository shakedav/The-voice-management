import {Component, OnInit, Input} from '@angular/core';
import {TeamDTO} from "../../model/team.dto";
import {HttpService} from "../../services/http.service";
import {teamCandidatesURL} from "../../consts/urls";
import {CandidateDTO} from "../../model/candidate.dto";

@Component({
  selector: 'mentor-team',
  template: ` <div class="mentor-team" *ngIf= "team.isVisible" >
                <div class="team-box"> 
                <div class="microphone-image-container">
                  <img class="microphone-image" src="../../../assets/images/microphone.png"/>
                </div>
                <div>
                  <div class="team-title title">{{team.name}}</div>
                </div>
                </div>
                <div style="display: flex; flex-direction: row" >
                    <candidates-list [candidates]="candidates"></candidates-list>
                </div>
              </div>
`,
  styleUrls: ['team.component.css']
})
export class TeamComponent implements OnInit {

  @Input() team: TeamDTO;
  private candidates: CandidateDTO;
  private mentorID;
  constructor(private httpService: HttpService) {
  }

  ngOnInit() {
    this.mentorID = this.team.mentorID;
    this.httpService.get(teamCandidatesURL.replace('$teamID', this.team.teamID.toString()))
      .subscribe(
        candidates => this.candidates = candidates,
        error => console.error(error));
  }
}
