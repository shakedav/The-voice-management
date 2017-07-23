import { Component, OnInit } from '@angular/core';
import {HttpService} from "../services/http.service";
import {activitiesUrl} from "../consts/urls";
import {ActivatedRoute} from "@angular/router";
import {ActivityDTO} from "../model/activity.dto";
import {CandidateDTO} from "../model/candidate.dto";

@Component({
  selector: 'app-activities-list',
  template: `
              <div class="activities-container">
                <candidate-activities *ngIf="activities" [candidateActivities]="activities" [candidate]="candidate"></candidate-activities>
              </div>
`,
  styleUrls: ['activities-list.component.css']
})
export class ActivitiesListComponent implements OnInit {
  private candidate: CandidateDTO;
  private activities: ActivityDTO;

  constructor(private httpService: HttpService, private route: ActivatedRoute) {

  }

  ngOnInit() {
      this.candidate = JSON.parse(localStorage.getItem('candidate'));

      this.httpService.get(activitiesUrl + this.candidate.candidateID)
      .subscribe(
        activity => this.activities = activity,
        error => console.error(error) );
  }
}
