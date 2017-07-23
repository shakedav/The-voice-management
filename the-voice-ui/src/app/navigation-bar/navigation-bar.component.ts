import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'navigation-bar',
  template: `
         <div class="top-pane">
            <span class="app-name">
              <img class="logo" src="../../../assets/images/The-Voice-Logo-620x360.png"/> 
              <!--<img class="logo" src="../../../assets/images/The_Voice_Australia_2017_logo.png"/>-->
            </span>
            <div class="top-pane-navigation-menu">              
              <span (click)="navigateToPage('')">Home</span>
              <span (click)="navigateToPage('teams')">Teams</span>
              <span (click)="navigateToPage('teams')">Candidates</span>
              <span (click)="navigateToPage('activities')">Activities</span>
            </div>
          </div>
`,
  styleUrls: ['./navigation-bar.component.css']
})
export class NavigationBarComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit() {
  }

  public navigateToPage(url: string){
    this.router.navigate([url]);
  }

}
