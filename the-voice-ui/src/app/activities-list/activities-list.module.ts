import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivitiesListComponent } from './activities-list.component';
import {CandidateActivitiesComponent} from "./candidate-activities/candidate-activities.component";

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ActivitiesListComponent, CandidateActivitiesComponent]
})
export class ActivitiesListModule { }
