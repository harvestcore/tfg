import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {AuthService} from '../../services/auth.service';
import {BasicAuth} from '../../interfaces/basic-auth';
import {UserService} from '../../services/user.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm: any;
  client: string;
  username: string;
  password: string;

  showFeedback = false;

  constructor(
    private authService: AuthService,
    private userService: UserService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      client: new FormControl(this.client, []),
      username: new FormControl(this.username, [
        Validators.required,
        Validators.minLength(1)
      ]),
      password: new FormControl(this.password, [
        Validators.required,
        Validators.minLength(1)
      ])
    });
  }

  resetFeedback() {
    this.showFeedback = false;
  }

  onSubmit(data: BasicAuth) {
    this.authService.login(data).subscribe(response => {
      if (response.ok) {
        this.userService.setCurrentUser(data.username).subscribe(() => {
            this.showFeedback = false;
            this.router.navigateByUrl('/');
        });
      } else {
        this.showFeedback = true;
      }
    });
  }
}
