import { Component, OnInit } from '@angular/core';
import {AuthService} from '../../services/auth.service';
import {Router} from '@angular/router';
import {UserService} from '../../services/user.service';

@Component({
  selector: 'app-top-navigator',
  templateUrl: './top-navigator.component.html',
  styleUrls: ['./top-navigator.component.scss']
})
export class TopNavigatorComponent implements OnInit {

  constructor(
    private router: Router,
    private authService: AuthService,
    private userService: UserService
  ) { }

  ngOnInit(): void {
  }

  handleLogout() {
    this.authService.logout().subscribe(data => {
      this.userService.clearCurrentUser();
      this.router.navigateByUrl('/login');
    });
  }
}
