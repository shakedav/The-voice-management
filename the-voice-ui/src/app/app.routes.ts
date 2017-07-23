

import {Routes} from "@angular/router";
import {AppComponent} from "./app.component";
import {TeamsListComponent} from "./teams-list/teams-list.component";
import {LoginComponent} from "./login/login.component";
import {ActivitiesListComponent} from "./activities-list/activities-list.component";

export const routes: Routes = [
  { path: '', component: LoginComponent},
  { path: 'teams', component: TeamsListComponent },
  { path: 'activities', component: ActivitiesListComponent }
]
