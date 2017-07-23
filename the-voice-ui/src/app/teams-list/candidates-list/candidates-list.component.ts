import {Component, OnInit, Input} from '@angular/core';
import {CandidateDTO} from "../../model/candidate.dto";
import {HttpService} from "../../services/http.service";
import {Router} from "@angular/router";

@Component({
  selector: 'candidates-list',
  template: `                
                <div class="candidates-container"> 
                  <div class="candidates" *ngFor="let candidate of candidates" (click)="getCandidateActivities(candidate)">
                    <div class="candidate-container">
                      <div class="candidate-link">
                        <div>
                       <div class="candidate-details">
                          <img class="singing-man-icon" src="../../../assets/images/avatar.png" />
                            <div>{{candidate.candidateName}}</div>        
                        </div>
                        </div>
                      </div>                                                                                                                    
                    </div>
                  </div>
                </div>
`,
  styleUrls: ['./candidates-list.component.css']
})
export class CandidatesListComponent implements OnInit {

  @Input() candidates: CandidateDTO;

  constructor(private httpService: HttpService, private router: Router) {

  }

  ngOnInit() {

  }

  private getCandidateActivities(candidate: CandidateDTO) {
    localStorage.setItem('candidate', JSON.stringify(candidate));
    this.router.navigate(['activities']);
  }

}
