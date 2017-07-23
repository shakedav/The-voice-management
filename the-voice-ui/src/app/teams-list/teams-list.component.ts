import {Component, OnInit, Input} from '@angular/core';
import {CandidateDTO} from "../model/candidate.dto";
import {HttpService} from "../services/http.service";
import {candidatesUrl, activitiesUrl, mentorTeamsUrl, teamCandidatesURL, teamsUrl} from "../consts/urls";
import {ActivityDTO} from "../model/activity.dto";
import {TeamDTO} from "../model/team.dto";

@Component({
  selector: 'app-teams-list',
  template: `              
              <div *ngIf="isAdmin" class="admin-filter">
                  <div *ngFor="let team of teams">
                    <button (click)="filterTeam(team)">{{team.name}}</button>
                  </div>
              </div>  
              <div class="">
                <div>
                </div>
                 <div class="teams-container">                  
                    <mentor-team *ngFor="let mentorTeam of teams" [team]="mentorTeam"></mentor-team>                  
                </div>
                </div>         
`,
  styleUrls: ['teams-list.component.css']
})
export class TeamsListComponent implements OnInit {

  public teams: TeamDTO[];
  public isAdmin: boolean;
  private mentorID;
  private teamsURL: string;

  constructor(private httpService: HttpService) {
    const userType = JSON.parse(localStorage.getItem('userType'));
    this.mentorID = JSON.parse(localStorage.getItem('mentorID'));
    if (this.mentorID > 0) {
      this.teamsURL = mentorTeamsUrl.replace('$mentorID', this.mentorID.toString() )
    }
    else
      this.teamsURL = teamsUrl;
    switch (userType) {
      case 'Admin':
        this.isAdmin = true;
        break;
      default:
        this.isAdmin = false;
    }
  }

  ngOnInit() {
    this.httpService.get(this.teamsURL)
      .subscribe(
        teams => this.teams= teams,
        error => console.error(error));
  }

  public filterTeam(team: TeamDTO) {
    var index = this.teams.indexOf(team);
    this.teams[index].isVisible = !this.teams[index].isVisible;
  }
}
