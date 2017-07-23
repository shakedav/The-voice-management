import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TeamsListComponent } from './teams-list.component';
import {TeamComponent} from "./team/team.component";
import { CandidatesListComponent } from './candidates-list/candidates-list.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [TeamsListComponent, TeamComponent, CandidatesListComponent
  ]
})
export class TeamsListModule { }
