import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: ` 
              <navigation-bar></navigation-bar>
              <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent {
}
