import { Component, OnInit } from '@angular/core';
import {HttpService} from "../services/http.service";
import {Router} from "@angular/router";
import {loginUrl} from "../consts/urls";
import {FormGroup, Validators, FormBuilder} from "@angular/forms";
import {UserDetails} from "../model/userDetails";

@Component({
  selector: 'app-login',
  providers: [HttpService],
  template: `

<div class="login-container">

  <form [formGroup]="loginForm" >
  <div [hidden]="!errorMessage">{{errorMessage}}</div>
  <h2 class="welcome-message">Welcome!</h2>
  <div class="group">
    <input type="text" for="username" formControlName="username"><span class="highlight"></span><span class="bar"></span>
    <label>Name</label>
  </div>
  <div class="group">
    <input type="password" formControlName="password" for="password"><span class="highlight"></span><span class="bar"></span>
    <label>Password</label>
  </div>
  <button type="button" (click)="login(loginForm)" class="button buttonBlue">Login</button>
</form>
  <div class="the-voice-image">
                  <img src="../../assets/images/TheVoice.jpg" />                
                </div>
              </div>
            `,
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public loginForm: FormGroup;
  private userDetails: UserDetails;
  private errorMessage: string = null;

  constructor(private httpService:HttpService,
              private formBuilder: FormBuilder,
              private router: Router
  )
  {

  }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    })

  }

  login(formDetails: any) {
    this.errorMessage = null;
    let loginDetails = formDetails.value;
    let loginFormDetails: UserDetails = new UserDetails(loginDetails.username, loginDetails.password);
    this.httpService.post(loginUrl, loginFormDetails)
      .subscribe(
        userDetails => {
          this.userDetails = userDetails
          console.log(this.userDetails);
          localStorage.setItem('userType', JSON.stringify(userDetails[0].userType));
          localStorage.setItem('mentorID', JSON.stringify(userDetails[0].mentorId));
          this.router.navigate(['teams'])
        },
           error => {
            this.errorMessage = error;
            console.error(error)
        } );
  }
}

