import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../../services/auth.service';
import { UserService } from '../../services/user.service';

import { User } from '../../interfaces/user';

@Component({
  selector: 'app-top-navigator',
  templateUrl: './top-navigator.component.html',
  styleUrls: ['./top-navigator.component.scss']
})
export class TopNavigatorComponent implements OnInit {
  currentUser: User;

  constructor(
    private router: Router,
    private authService: AuthService,
    private userService: UserService
  ) {
    this.authService.loginStateChangedNotifier.subscribe(() => {
      this.updateToolbarData();
    });
  }

  ngOnInit(): void {
  }

  updateToolbarData() {
    this.currentUser = this.userService.getCurrentUser();
  }

  handleLogout() {
    this.authService.logout().subscribe(data => {
      this.userService.clearCurrentUser();
      this.authService.loginStateChangedNotifier.emit();
      this.router.navigateByUrl('/login');
    });
  }
}
