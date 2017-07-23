import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {RouterModule} from "@angular/router";
import {routes} from "./app.routes";
import {TeamsListModule} from "./teams-list/teams-list.module";
import {LoginModule} from "./login/login.module";
import {HttpModule} from "@angular/http";
import {HttpService} from "./services/http.service";
import {ActivitiesListModule} from "./activities-list/activities-list.module";
import {NavigationBarComponent} from "./navigation-bar/navigation-bar.component";

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    LoginModule,
    HttpModule,
    TeamsListModule,
    ActivitiesListModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
