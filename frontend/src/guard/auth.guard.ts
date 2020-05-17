import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';

import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private userService: UserService,
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    return this.checkAccess(state.url);
  }

  checkAccess(url: string): boolean {
    let canAccess = false;

    if (url.includes('login')) {
      this.authService.login().subscribe(response => {
        if (response.ok) {
          this.router.navigateByUrl('/');
        }
      });

      canAccess = true;
    } else {
      if (this.userService.userLoggedIn()) {
        canAccess = true;
      } else {
        this.authService.login().subscribe(response => {
          canAccess = response.ok;
          if (!canAccess) {
            this.router.navigateByUrl('/login');
          }
        });
      }
    }

    return canAccess;
  }

}
