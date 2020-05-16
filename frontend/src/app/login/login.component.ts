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
  username: string;
  password: string;

  constructor(
    private authService: AuthService,
    private userService: UserService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loginForm = new FormGroup({
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

  onSubmit(data: BasicAuth) {
    this.authService.login(data).subscribe(token => {
      if (token.ok) {
        this.userService.setCurrentUser(data.username);
        const urlToRedirect = this.authService.getUrlToRedirect();
        if (urlToRedirect) {
          this.router.navigate([urlToRedirect]);
        } else {
          this.router.navigate(['/']);
        }
      }
    });
  }
}
