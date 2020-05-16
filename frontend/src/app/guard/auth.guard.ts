import { Injectable } from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router} from '@angular/router';

import { AuthService } from '../../services/auth.service';
import { UserService } from '../../services/user.service';

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
    if (url.includes('/login')) {
      return this.userService.userLoggedIn();
    } else {
      if (this.userService.userLoggedIn()) {
        const currentUser = this.userService.getCurrentUser();
        return currentUser && currentUser.type === 'admin';
      }
      this.authService.setUrlToRedirect(url);
    }

    this.router.navigate(['/login']);
    return false;
  }

}
