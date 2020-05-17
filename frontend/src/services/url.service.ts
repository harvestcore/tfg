import { Injectable } from '@angular/core';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UrlService {

  private client: string;

  constructor() { }

  setClient(client: string) {
    this.client = client;
  }

  getBackendUrl(): string {
    let protocol = 'http://';
    let client = '';
    if (environment.httpsEnabled) {
      protocol = 'https://';
    }

    if (this.client) {
      client = this.client + '.';
    }

    return protocol + client + environment.backendUrl;
  }
}
