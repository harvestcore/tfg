import { Injectable } from '@angular/core';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UrlService {
  private browserWindow = window || {};
  // tslint:disable-next-line:no-string-literal
  private env = this.browserWindow['__env'] || null;
  private client: string;

  constructor() { }

  setClient(client: string) {
    this.client = client;
  }

  getBackendUrl(): string {
    let protocol = 'http://';
    let client = '';
    let backendUrl: string;

    if (this.env && this.env.backendUrl) {
      backendUrl = this.env.backendUrl;
      if (this.env.httpsEnabled) {
        protocol = 'https://';
      }
    } else {
      backendUrl = environment.backendUrl;
      if (environment.httpsEnabled) {
        protocol = 'https://';
      }
    }

    if (this.client) {
      client = this.client + '.';
    }

    return protocol + client + backendUrl;
  }
}
